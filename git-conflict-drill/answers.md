

### 1. When would you rebase and when would you merge?

I use **merge** when combining branches while preserving their complete development history. It is useful for team collaboration because it retains original commits and records when branches were integrated. I use **rebase** when updating my personal feature branch with the latest changes from the main branch. It creates a cleaner, linear commit history by replaying my commits on top of the updated branch. However, I avoid rebasing commits that have already been shared with others because it changes commit hashes and can cause collaboration issues. In short, merge preserves branch history, while rebase creates a cleaner history.

### 2. You have committed a password and pushed it. Walk me through what you do.

First, I immediately revoke or change the exposed password because deleting it from Git does not make it secure again. Then, I remove it from the source code and store the replacement in environment variables or a secrets manager. If necessary, I clean the Git history using a history-rewriting tool and coordinate with collaborators before force-pushing. I also ensure that team members synchronize their repositories safely. Finally, I scan the repository for other exposed secrets and enable secret scanning to prevent similar incidents in the future.

### 3. What is the staging area for?

The staging area is an intermediate space between the working directory and the Git repository. It allows developers to select which changes should be included in the next commit. Using `git add`, I can stage specific files or selected changes instead of committing every modification. For example, if I modify three files but want to commit only two, I can stage those two files separately. When I run `git commit`, Git saves the staged changes as a new commit. The staging area helps create smaller, organized commits and provides better control over project history.