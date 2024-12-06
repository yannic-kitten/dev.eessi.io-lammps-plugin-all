# `dev.eessi.io` Example Project

This is an example repository for the setup of the build and ingestion process for EESSI's `dev.eessi.io` CernVM-FS repository. It is primarily intended for the [MultiXscale CoE](https://multixscale.eu) partners working on the development of the project's core applications.

`dev.eessi.io` project repositories are hosted on GitHub and follow the naming convention: `dev.eessi.io-projectname`. Once built and ingested, installations for each project will be available in systems that have EESSI available under `/cvmfs/dev.eessi.io/2023.06/projectname/`, where `2023.06` corresponds to the matching version of EESSI's `software.eessi.io` repository and [compatibility layer](https://github.com/EESSI/filesystem-layer).

## Installation instructions for new project repositories

This section details the steps needed to setup the infrastructure for a new project's repository and bot.
