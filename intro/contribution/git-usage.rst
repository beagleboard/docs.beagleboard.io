.. _beagleboard-git-usage:

Git Usage
#########

.. note:: 
    For detailed information on Git and Gitlab checkout the official 
    `Git and GitLab <https://git.beagleboard.org/help#git-and-gitlab>`_ 
    help page. Also, for good GitLab workflow you can checkout the 
    `Introduction to GitLab Flow (FREE) <https://git.beagleboard.org/help/topics/gitlab_flow.md>`_ page.

These are (draft) general guidelines taken from 
`BioPython project <https://biopython.org/wiki/GitUsage>`_ 
to be used for BeagleBoard development using
git. We're still working on the finer details.

This document is meant as an outline of the way BeagleBoard projects are developed.
It should include all essential technical information as well as typical
procedures and usage scenarios. It should be helpful for core
developers, potential code contributors, testers and everybody
interested in BeagleBoard code.

.. note:: This version is an unofficial draft and is subject to change.

Relevance
---------------

This page is about actually using git for tracking changes.

If you have found a problem with any BeagleBoard project, and think you know how to
fix it, then we suggest following the simple route of filing a
bug and describe your fix. Ideally, you would upload a patch file showing the differences
between the latest version of BeagleBoard project (from our repository) and your
modified version. Working with the command line tools *diff* and *patch*
is a very useful skill to have, and is almost a precursor to working
with a version control system.


Technicalities
-----------------

This section describes technical introduction into git usage including
required software and integration with GitLab. If you want to start
contributing to BeagleBoard, you definitely need to install git and learn
how to obtain a branch of the BeagleBoard project you want to contribute. 
If you want to share your changes easily with others, you should also 
sign up for a `BeagleBoard GitLab <https://git.beagleboard.org/users/sign_up>`_ 
account and read the corresponding section of the manual. Finally, if you are
engaged in one of the collaborations on experimental BeagleBoard modules,
you should look also into code review and branch merging.

Installing Git
-----------------

You will need to install Git on your computer. `Git <http://git-scm.com/>`_
is available for all major operating systems. Please use the appropriate
installation method as described below.

Linux
******

Git is now packaged in all major Linux distributions, you should find it
in your package manager.

Ubuntu/Debian
**************

You can install Git from the `git-core` package. e.g.,

.. code-block::

    sudo apt-get install git-core


You'll probably also want to install the following packages: `gitk`,
`git-gui`, and `git-doc`

Redhat/Fedora/Mandriva
**************************

git is also packaged in rpm-based linux distributions.

.. code-block::

    dnf install gitk

should do the trick for you in any recent fedora/mandriva or
derivatives

Mac OS X
**********

Download the `.dmg` disk image from
http://code.google.com/p/git-osx-installer/

Windows
********

Download the official installers from
`Windows installers <https://git-scm.com/download/win>`_

Testing your git installation
-------------------------------

If your installation succeeded, you should be able to run


.. code-block::

    $ git --help

in a console window to obtain information on git usage. If this fails,
you should refer to git
`documentation <https://git-scm.com/doc>`_ for troubleshooting.

Creating a GitLab account (Optional)
--------------------------------------

Once you have Git installed on your machine, you can obtain the code and
start developing. Since the code is hosted at GitLab, however, you may
wish to take advantage of the site's offered features by signing up for
a GitLab account. While a GitLab account is completely optional and not
required for obtaining the BeagleBoard code or participating in
development, a GitLab account will enable all other BeagleBoard developers
to track (and review) your changes to the code base, and will help you
track other developers' contributions. This fosters a social,
collaborative environment for the BeagleBoard community.

If you don't already have a GitLab account, you can create one
`here <https://git.beagleboard.org/users/sign_up>`_.
Once you have created your account, upload an SSH public key by clicking
on `SSH and GPG keys <https://git.beagleboard.org/-/profile/keys>` after logging in. For more
information on generating and uploading an SSH public key, see `this
GitLab guide <https://docs.gitlab.com/ee/user/ssh.html>`_.

Working with the source code
---------------------------------

In order to start working with the BeagleBoard source code, you need to
obtain a local clone of our git repository. In git, this means you will
in fact obtain a complete clone of our git repository along with the
full version history. Thanks to compression, this is not much bigger
than a single copy of the tree, but you need to accept a small overhead
in terms of disk space.

There are, roughly speaking, two ways of getting the source code tree
onto your machine: by simply "cloning" the repository, or by "forking"
the repository on GitLab. They're not that different, in fact both will
result in a directory on your machine containing a full copy of the
repository. However, if you have a GitLab account, you can make your
repository a public branch of the project. If you do so, other people
will be able to easily review your code, make their own branches from it
or merge it back to the trunk.

Using branches on GitLab is the preferred way to work on new features
for BeagleBoard, so it's useful to learn it and use it even if you think
your changes are not for immediate inclusion into the main trunk of
BeagleBoard. But even if you decide not to use GitLab, you can always
change this later (using the .git/config file in your branch.) For
simplicity, we describe these two possibilities separately.

Cloning BeagleBoard directly
-----------------------------

Getting a copy of the repository (called "cloning" in Git terminology)
without GitLab account is very simple:

.. code-block::

    git clone https://git.beagleboard.org/docs/docs.beagleboard.io.git

This command creates a local copy of the entire BeagleBoard repository on
your machine (your own personal copy of the official repository with its
complete history). You can now make local changes and commit them to
this local copy (although we advise you to use named branches for this,
and keep the main branch in sync with the official BeagleBoard code).

If you want other people to see your changes, however, you must publish
your repository to a public server yourself (e.g. on GitLab).

Forking BeagleBoard with your GitLab account
----------------------------------------------

If you are logged in to GitLab, you can go to the BeagleBoard Docs repository
page:

https://git.beagleboard.org/docs/docs.beagleboard.io/-/tree/main

and click on a button named 'Fork'. This will create a fork (basically a
copy) of the official BeagleBoard repository, publicly viewable on GitLab,
but listed under your personal account. It should be visible under a URL
that looks like this:

https://git.beagleboard.org/yourusername/docs.beagleboard.io/

Since your new BeagleBoard repository is publicly visible, it's considered
good practice to change the description and homepage fields to something
meaningful (i.e. different from the ones copied from the official
repository).

If you haven't done so already, setup an SSH key and `upload it to
gitlab <https://docs.gitlab.com/ee/user/ssh.html>`_ for
authentication.

Now, assuming that you have git installed on your computer, execute the
following commands locally on your machine. This "url" is given on the
GitLab page for your repository (if you are logged in):

.. code-block::

    git clone https://git.beagleboard.org/yourusername/docs.beagleboard.io.git

Where `yourusername`, not surprisingly, stands for your GitLab username.
You have just created a local copy of the BeagleBoard Docs repository on your
machine.

You may want to also link your branch with the official distribution
(see below on how to keep your copy in sync):

.. code-block::

    git remote add upstream https://git.beagleboard.org/docs/docs.beagleboard.io/

If you haven't already done so, tell git your name and the email address
you are using on GitLab (so that your commits get matched up to your
GitLab account). For example,

.. code-block::

    git config --global user.name "David Jones" config --global user.email "d.jones@example.com"


Making changes locally
-------------------------

Now you can make changes to your local repository - you can do this
offline, and you can commit your changes as often as you like. In fact,
you should commit as often as possible, because smaller commits are much
better to manage and document.

First of all, create a new branch to make some changes in, and switch to
it:

.. code-block::

    git branch demo-branch checkout demo-branch

To check which branch you are on, use:

.. code-block::

    git branch

Let us assume you've made changes to the file beaglebone-black/ch01.rst Try this:

.. code-block::

    git status

So commit this change you first need to explicitly add this file to your
change-set:

.. code-block::

    git add beaglebone-black/ch01.rst

and now you commit:

.. code-block::

    git commit -m "added updates X in BeagleBone Black ch01"

Your commits in Git are local, i.e. they affect only your working branch
on your computer, and not the whole BeagleBoard tree or even your fork on
GitLab. You don't need an internet connection to commit, so you can do
it very often.

Pushing changes to GitLab
----------------------------

If you are using GitLab, and you are working on a clone of your own
branch, you can very easily make your changes available for others.

Once you think your changes are stable and should be reviewed by others,
you can push your changes back to the GitLab server:

.. code-block::

    git push origin demo-branch

*This will not work if you have cloned directly from the official
BeagleBoard branch, since only the core developers will have write access
to the main repository.*

Merging upstream changes
--------------------------

We recommend that you don't actually make any changes to the **main**
branch in your local repository (or your fork onGitLab). Instead, use
named branches to do any of your own work. The advantage of this
approach it is the trivial to pull the upstream **main** (i.e. the
official BeagleBoard branch) to your repository.

Assuming you have issued this command (you only need to do this once):

.. code-block::

    git remote add upstream https://git.beagleboard.org/docs/docs.beagleboard.io/

Then all you need to do is:

.. code-block::

    git checkout main pull upstream main

Provided you never commit any change to your local **main** branch,
this should always be a simple *fast forward* merge without any
conflicts. You can then deal with merging the upstream changes from your
local main branch into your local branches (and you can do that
offline).

If you have your repository hosted online (e.g. at GitLab), then push
the updated main branch there:

.. code-block::

    git push origin main

Submitting changes for inclusion in BeagleBoard
-------------------------------------------------

If you think you changes are worth including in the main BeagleBoard
distribution, then file an (enhancement) bug on our bug
tracker, and include a link to your updated branch (i.e. your branch on 
GitLab, or another public Git server). You could also attach a patch to the bug. 
If the changes are accepted, one of the BeagleBoard developers will have to check
this code into our main repository.

On GitLab itself, you can inform keepers of the main branch of your
changes by sending a 'pull request' from the main page of your branch.
Once the file has been committed to the main branch, you may want to
delete your now redundant bug fix branch on GitLab.

If other things have happened since you began your work, it may require
merging when applied to the official repository's main branch. In this
case we might ask you to help by rebasing your work:

.. code-block::

    git fetch upstream checkout demo-branch
    
    git rebase upstream/main

Hopefully the only changes between your branch and the official repository's
main branch are trivial and git will handle everything automatically.
If not, you would have to deal with the clashes manually. If this works,
you can update the pull request by replacing the existing (pre-rebase)
branch:

.. code-block::

    git push origin demo-branch --force

If however the rebase does not go smoothly, give up with the following command
(and hopefully the BeagleBoard developers can sort out the rebase or merge for you):

.. code-block::

    git rebase --abort

Evaluating changes
------------------

Since git is a fully distributed version control system, anyone can
integrate changes from other people, assuming that they are using
branches derived from a common root. This is especially useful for
people working on new features who want to accept contributions from
other people.

This section is going to be of particular interest for the BeagleBoard
core developers, or anyone accepting changes on a branch.

For example, suppose Jason has some interesting changes on his public
repository:

https://git.beagleboard.org/jkridner/docs.beagleboard.io

You must tell git about this by creating a reference to this remote
repository:

.. code-block::

    git remote add jkridner https://git.beagleboard.org/jkridner/BeagleBoard.git

Now we can fetch *all* of Jason's public repository with one line:

.. code-block::

    git fetch jkridner

Now we can run a diff between any of our own branches and any of Jason's
branches. You can list your own branches with:

.. code-block::

    git branch

Remember the asterisk shows which branch is currently checked out.

To list the remote branches you have setup:

.. code-block::

    git branch -r

For example, to show the difference between your **main** branch and
Jason's **main** branch:

.. code-block::

    git diff main jkridner/main

If you are both keeping your **main** branch in sync with the upstream
BeagleBoard repository, then his **main** branch won't be very
interesting. Instead, try:

.. code-block::

    git diff main jkridner/awesomebranch

You might now want to merge in (some) of Jason's changes to a new branch
on your local repository. To make a copy of the branch (e.g. awesomebranch)
in your local repository, type:

.. code-block::

    git checkout --track jkridner/awesomebranch

If Jason is adding more commits to his remote branch and you want to update
your local copy, just do:

.. code-block::

    git checkout awesomebranch  # if you are not already in branch awesomebranch pull

If you later want to remove the reference to this particular branch:

.. code-block::

    git branch -r -d jkridner/awesomebranch
    Deleted remote branch jkridner/awesomebranch (#######)

Or, to delete the references to all of Jason's branches:

.. code-block::

    git remote rm jkridner
    
    git branch -r
        upstream/main
        origin/HEAD
        origin/main

Alternatively, from within GitLab you can use the fork-queue to cherry
pick commits from other people's forked branches. While this
defaults to applying the changes to your current branch, you would
typically do this using a new integration branch, then fetch it to your
local machine to test everything, before merging it to your main branch.

Committing changes to main branch
---------------------------------

This section is intended for BeagleBoard developers, who are allowed to
commit changes to the BeagleBoard main "official" branch. It describes the
typical activities, such as merging contributed code changes both from
git branches and patch files.

Prerequisites
-------------

Currently, the main BeagleBoard branch is hosted on GitLab. In order to
make changes to the main branch you need a GitLab account and you need
to be added as a collaborator/Maintainer to the BeagleBoard account. 
This needs to be done only once. If you have a GitLab account, but you are not yet a
collaborator/Maintainer and you think you should be ask Jason to be added (this is meant for
regular contributors, so in case you have only a single change to make,
please consider submitting your changes through one of developers).

Once you are a collaborator/Maintainer, you can pull BeagleBoard official branch
using the private url. If you want to make a new repository (linked to
the main branch), you can just clone it:

.. code-block::

    git clone https://git.beagleboard.org/lorforlinux/docs.beagleboard.io.git

It creates a new directory "BeagleBoard" with a local copy of the official
branch. It also sets the "origin" to the GitLab copy This is the
recommended way (at least for the beginning) as it minimizes the risk of
accidentally pushing changes to the official GitLab branch.

Alternatively, if you already have a working git repo (containing your
branch and your own changes), you can add a link to the official branch
with the git "remote command"... but we'll not cover that here.

In the following sections, we assume you have followed the recommended
scenario and you have the following entries in your .git/config file:

.. code-block::

    [remote "origin"]
        url = https://git.beagleboard.org/lorforlinux/docs.beagleboard.io.git

    [branch "main"]
        remote = origin

Committing a patch
------------------

If you are committing from a patch, it's also quite easy. First make
sure you are up to date with official branch:

.. code-block::

    git checkout main pull origin

Then do your changes, i.e. apply the patch:

.. code-block::

    patch -r someones_cool_feature.diff

If you see that there were some files added to the tree, please add them
to git:

.. code-block::

    git add beaglebone-black/some_new_file

Then make a commit (after adding files):

.. code-block::

    git commit -a -m "committed a patch from a kind contributor adding feature X"

After your changes are committed, you can push toGitLab:

.. code-block::

    git push origin

Tagging the official branch
---------------------------

If you want to put tag on the current BeagleBoard official branch (this is
usually done to mark a new release), you need to follow these steps:

First make sure you are up to date with official branch:

.. code-block::

    git checkout main pull origin

Then add the actual tag:

.. code-block::

    git tag new_release

And push it to GitLab:

.. code-block::

    git push --tags origin main

Additional Resources
--------------------

There are a lot of different nice guides to using Git on the web:

-   `Understanding Git
    Conceptually <https://www.sbf5.com/~cduan/technical/git/>`_
-   `git ready: git tips <http://gitready.com/>`_
-   <http://http://cheat.errtheblog.com/s/git>
-   https://docs.scipy.org/doc/numpy-1.15.1/dev/gitwash/development_workflow.html Numpy is also
    evaluating git
-   https://github.github.com/training-kit/downloads/github-git-cheat-sheet
-   https://lab.github.com/courses
-   `Pro Git <https://git-scm.com/book/en/v2>`_

