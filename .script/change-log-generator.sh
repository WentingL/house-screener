#!/bin/bash

# This script will build the CHANGELOG.MD file for the Protoss Project
# and commit it to the current branch.
#
# This tool should be run in the release candidate branch, and the running
# machine should have a couple dependencies installed first:
#
# * npm
# * conventional-changelog
# * conventional-changelog-cli
#
# Other required conditions:
#
# * The branch must be clean (no untracked changes)
# * The branch must be a release candidate branch

#GLOBALS

CHECK='\u2714'
CROSS='x'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' #color reset


# Logs a message to the console.
function message() {
  /usr/bin/printf "[CHANGELOG GENERATOR]: $1\n"
}

# Exits the script with an error code and an optional message
function error() {

  # $1 = Optional error message

  if [ -z "$1" ]
  then
    /usr/bin/printf "[ERROR]: ${RED}Exiting Script.${NC}\n"
  else
    /usr/bin/printf "[ERROR]: ${RED}${1}${NC}\n"
  fi
  exit 1
}

# Validates that all of the preconditions of the script are true
function validate() {

  message "Validating Preconditions."

  # ensure that NPM is installed
  if ! version=$(npm --version);
  then
    message "${RED}${CROSS}${NC} NPM Installed."
    error "NPM is not installed, please visit: https://nodejs.org/en/"
  else
    message "${GREEN}${CHECK}${NC} NPM ${version} Installed."
  fi

  # ensure the conventional-changelog-cli is installed
  if ! version=$(conventional-changelog --version);
  then
    message "${RED}${CROSS}${NC} Conventional Changelog Installed."
    error "Conventional Changelog is not installed, please run: npm i -g conventional-changelog && npm i -g conventional-changelog-cli"
  else
    message "${GREEN}${CHECK}${NC} Conventional Changelog ${version} Installed."
  fi

  # warn if we are not in master
  if [[ $BRANCH =~ ^master$ ]]
  then
    message "${GREEN}${CHECK}${NC} In master branch."
  else
    message "${RED}${CROSS}${NC} In master branch. ${YELLOW}You likely want to run this script on the master branch.${NC}"
  fi

  # ensure that there are no un-staged or un-commit changes
  if [[ $(git status --porcelain) ]]
  then
    message "${RED}${CROSS}${NC} No untracked changes."
    error "You have untracked changes. Please commit your changes and run the script again."
  else
    message "${GREEN}${CHECK}${NC} No untracked changes."
  fi

  message "${GREEN}${CHECK}${NC} All Preconditions Met."

}

# Boiler plate function to discover script directory
# and change to the project root
function locate_script() {

  SOURCE="${BASH_SOURCE[0]}"
  # resolve $SOURCE until the file is no longer a symlink
  while [ -h "$SOURCE" ]; do
    DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
    SOURCE="$(readlink "$SOURCE")"
    # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
    [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
  done
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

  # Change to project root so we can access the files we need
  cd "${DIR}/.." || exit
  message "Moving to $(pwd)"

}

# Resolve the directory the script is located in, so we can run it anywhere
# Store the current branch so we can re-check it out once we are done
function store_branch() {
  BRANCH=$(git symbolic-ref -q HEAD)
  BRANCH=${BRANCH##refs/heads/}
  BRANCH=${BRANCH:-HEAD}
}

# This function will roll back the state of the repo back to where
# the script began
function roll_back() {

  # $1 = message to pass to error

  git reset --hard
  error "$1"
}

# This function will remove local tags, and re-pull the tags from the remote
function sync_remote_tags() {
  message "Preparing Git Tags."
  git tag -l | xargs git tag -d > /dev/null 2>&1
  git fetch --tags > /dev/null 2>&1
  message "Remote Tags Synced."
}

# Conventional change log requires the tags in a specific format
# This function will rename and re-tag all existing tags (except FRE tags)
# to the expected format
function rename_tags() {

  message "Renaming Tags."
  for tag in $(git tag -l); do
    if echo "$tag" | grep -qv 'FRE'
    then
      new=$(echo "$tag" | cut -d'-' -f 3)
      git tag "v$new" "$tag"
      message "Retagging protoss-$tag"
    fi
  done

}

# This function will attempt to clean up the links in the changelog file
# to work with the actual tag format we use
function edit_changelog() {
  message "Editing CHANGELOG-new.md."

  # Rename the tags in the CHANGELOG-new.md file so the links work
  sed -i -e 's|house-screener/compare/v|house-screener/compare/house-screener-|g' CHANGELOG-new.md
  sed -i -e 's|\.\.\.v|...house-screener-|g' CHANGELOG-new.md

  # Prepend a static header
  echo -e "All notable changes to this project will be documented in this file. See [Conventional Commits](https:conventionalcommits.org/) for commit guidelines.\n\n$(cat CHANGELOG-new.md)" > CHANGELOG-new.md
  echo -e "# Change Log\n\n$(cat CHANGELOG-new.md)" > CHANGELOG-new.md
}

# This function will try to safely run the conventional changelog program
# Rolling back the repo if there are any errors
function run_changelog() {
  message "Generating CHANGELOG-new.md."
  if ! conventional-changelog -p angular -i CHANGELOG-new.md -s -r 0;
  then
    roll_back "Error running conventional-changelog."
  fi
}

# This function will prompt the user to approve the running of the script
function request_approval() {
  NC='\033[0m'
  message "${YELLOW}WARNING - This script will overwrite all local tags.${NC}"
  read -p "Are you sure you want to proceed? (y/n) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]
  then
   message "Exiting Script"
   exit 0
  fi
}

# Main driver for the script
function run() {
  message "Starting Changelog Generation."

  # prompt the user that their local tags will be overwritten
  request_approval

  # find the script directory, so we can run in project root
  locate_script

  # prepare global branch variable
  store_branch

  # ensure all pre-conditions are met
  validate

  # sync the tags from the repo
  sync_remote_tags

  # rename the tags for the changelog generation
  rename_tags

  # generate the changelog
  run_changelog

  # make some adjustments to the form the changelog output
  edit_changelog

  # re-sync the remote tags
  sync_remote_tags

  message "Changelog Generation Complete."
}

# Script Start
run
exit