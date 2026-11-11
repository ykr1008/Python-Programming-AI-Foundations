# Git Conflict, Undo, Merge and Rebase Drill

## Overview

This exercise was completed in a **throwaway repository** named `git-conflict-drill`. The purpose was to deliberately create a merge conflict, practise different ways of undoing commits, and compare merging with rebasing.

The repository was kept separate from other projects so that destructive commands such as `git reset --hard` could be tested safely.

---

# Part A – Conflict Drill

## 1. Create the repository and initial file

Initialised a repository with `main` as the default branch:

```powershell
git init -b main
```

Created `app.py`:

```python
def greet():
    return "Hello"

print(greet())
```

Staged and committed the file:

```powershell
git add app.py
git commit -m "Initial commit"
```

This created the starting point shared by both branches.

## 2. Create and commit the feature branch change

Created and switched to `feature-a`:

```powershell
git switch -c feature-a
```

Changed the return value in `greet()` to `"Hi there"`:

```python
def greet():
    return "Hi there"

print(greet())
```

Committed the change:

```powershell
git add app.py
git commit -m "Update greeting to Hi there"
```

## 3. Make a different change on main

Switched back to `main`:

```powershell
git switch main
```

Changed the same return line to `"Good day"`:

```python
def greet():
    return "Good day"

print(greet())
```

Committed this change:

```powershell
git add app.py
git commit -m "Update greeting to Good day"
```

At this point, both branches had changed the same line in different ways.

## 4. Merge and capture the conflict

Attempted to merge `feature-a` into `main`:

```powershell
git merge feature-a
```

Git reported:

```text
Auto-merging app.py
CONFLICT (content): Merge conflict in app.py
Automatic merge failed; fix conflicts and then commit the result.
```

The conflict markers in `app.py` were:

```python
def greet():
<<<<<<< HEAD
    return "Good Day"
=======
    return "Hi there"
>>>>>>> feature-a

print(greet())
```

**What the markers mean:**

- `<<<<<<< HEAD` marks the beginning of the version from the current branch (`main`).
- `=======` separates the two conflicting versions.
- `>>>>>>> feature-a` marks the end of the incoming version from `feature-a`.

Git could not automatically decide which greeting should be kept because both branches modified the same line.

## 5. Resolve and commit the conflict

Resolved the conflict by keeping `"Good day"` and removing all conflict markers:

```python
def greet():
    return "Good day"

print(greet())
```

Staged and committed the resolution:

```powershell
git add app.py
git commit -m "Resolve merge conflict in app.py"
```

Ran the program:

```powershell
python app.py
```

Output:

```text
Good day
```

## 6. Final commit graph

Command:

```powershell
git log --oneline --graph --all
```

Output:

```text
*   e43621f (HEAD -> main) Resolve merge conflict in app.py
|\
| * 0934c57 (feature-a) Update greeting to Hi there
* | d18cf23 Update greeting to Good day
|/
* 96441d7 Initial commit with greet function
```

**Explanation:** The two branches split from the initial commit. Each branch then received its own commit. The final merge commit joins the two lines of history. The graph shows that Git preserved both branch histories and recorded the conflict resolution in a separate merge commit.

---

# Part B – Undo Drill

The following commands were tested in the throwaway repository. The important difference is whether Git keeps the changes, removes them, or creates a new commit to reverse them.

## 1. Undo the last commit but keep changes staged

Command:

```powershell
git reset --soft HEAD~1
```

**What happened:**

- The latest commit was removed from the current branch history.
- The changes from that commit remained in the staging area.
- `git status` showed the changes under **Changes to be committed**.

**Use case:** When a commit was made too early or with the wrong commit message, but the changes are still ready to be committed again.

## 2. Undo the last commit and keep changes unstaged

Command:

```powershell
git reset --mixed HEAD~1
```

**What happened:**

- The latest commit was removed from the current branch history.
- The staging area was reset.
- Changes to previously tracked files remain in the working directory but become unstaged.
- In this test, `notes.txt` was a newly created file that had not existed in the previous commit, so it appeared as an **untracked file**.

**Use case:** When I want to undo a commit and review or modify the changes before staging them again.

## 3. Discard the last commit and its tracked changes

Command:

```powershell
git reset --hard HEAD~1
```

**What happened:**

- The latest commit was removed from the current branch history.
- Tracked files were reset to match the target commit.
- The committed changes were discarded from the working tree.
- In the test, `Test-Path temp.txt` returned `False` because the file had been introduced by the discarded commit and did not exist in the target commit.

**Use case:** When I intentionally want to discard a local commit and its tracked changes.

**Warning:** `--hard` is destructive. It can discard uncommitted changes to tracked files. Untracked files are not automatically removed by `git reset --hard`.

## 4. Undo a commit that has already been pushed

A local bare repository was used as the remote for this test. After pushing a commit that added a temporary comment, the following command was run:

```powershell
git revert HEAD
```

Git created a new commit that reversed the changes introduced by the previous commit. The revert commit was then pushed:

```powershell
git push
```

Relevant commit history:

```text
14895e9 (HEAD -> main, origin/main) Revert "Add temporary comment"
997fa3d Add temporary comment
```

**What happened:**

- The original pushed commit remained in the history.
- Git created a new commit that undid its changes.
- The new revert commit was pushed to the remote.

**Use case:** This is the safer approach for undoing changes that have already been shared with others because it does not rewrite published history.

## Undo commands compared

| Command | Commit removed from current branch? | What happens to changes? |
|---|---:|---|
| `git reset --soft HEAD~1` | Yes | Kept staged |
| `git reset --mixed HEAD~1` | Yes | Kept unstaged |
| `git reset --hard HEAD~1` | Yes | Tracked changes discarded |
| `git revert HEAD` | No | Reversed in a new commit |

---

# Part C – Rebase vs Merge

## 1. Create two branches with different commits

Started from a common commit containing `project.txt`:

```text
Project started
```

Created `merge-demo` and added `merge.txt`:

```text
This is the merge branch.
```

Created `rebase-demo` from the same starting point and added `rebase.txt`:

```text
This is the rebase branch.
```

Meanwhile, `main` was updated by changing `project.txt` to:

```text
Project started
Main branch update
```

The main-branch change was committed before integrating either feature branch.

## 2. Merge the first branch

Switched to `main` and merged `merge-demo`:

```powershell
git switch main
git merge merge-demo
```

Git created a merge commit:

```text
8ecd666 Merge branch 'merge-demo'
```

### Merge graph

Command:

```powershell
git log --oneline --graph
```

Output after the merge:

```text
*   8ecd666 (HEAD -> main) Merge branch 'merge-demo'
|\
| * a2ab3d3 (merge-demo) Add merge branch feature
* | 897855c Update project on main
|/
* cb013b3 Add project starting point
* 14895e9 Revert "Add temporary comment"
* 997fa3d Add temporary comment
*   e43621f Resolve merge conflict in app.py
|\
| * 0934c57 Add greeting to Hi there
* | d18cf23 Update greeting to Good day
|/
* 96441d7 Initial commit with greet function
```

## 3. Rebase the second branch

Switched to `rebase-demo` and rebased it onto `main`:

```powershell
git switch rebase-demo
git rebase main
```

Git replayed the feature commit on top of the latest `main` commit.

### Rebase graph

Command:

```powershell
git log --oneline --graph
```

Output after the rebase:

```text
* 60f74ea (HEAD -> rebase-demo) Add rebase branch feature
*   8ecd666 (main) Merge branch 'merge-demo'
|\
| * a2ab3d3 (merge-demo) Add merge branch feature
* | 897855c Update project on main
|/
* cb013b3 Add project starting point
* 14895e9 Revert "Add temporary comment"
* 997fa3d Add temporary comment
*   e43621f Resolve merge conflict in app.py
|\
| * 0934c57 Add greeting to Hi there
* | d18cf23 Update greeting to Good day
|/
* 96441d7 Initial commit with greet function
```

## 4. Compare the graph shapes and commit hashes

| Aspect | Merge | Rebase |
|---|---|---|
| History | Preserves the branch's original history | Replays commits on top of the target branch |
| Graph | Shows diverging and joining branches | Produces a more linear feature-branch history |
| New commit | Creates a merge commit when a true merge is needed | Creates new commit(s) while replaying changes |
| Existing commit hashes | Existing commits are preserved | Replayed commits receive new hashes |

The rebase branch's reflog showed the original and new commit hashes:

```text
60f74ea (HEAD -> rebase-demo) rebase-demo@{0}: rebase (finish): refs/heads/rebase-demo onto 8ecd666f717c27a9341c179adb13fc3412ae7c6a
ea262f4 rebase-demo@{1}: commit: Add rebase branch feature
cb013b3 (origin/main) rebase-demo@{2}: branch: Created from HEAD
```

The original feature commit was `ea262f4`. After rebasing, the recreated commit was `60f74ea`.

**Why did the hash change?** A Git commit hash depends on the commit's contents and metadata, including its parent commit. Rebase replayed the change on top of a different parent, so Git created a new commit with a different hash even though the file change remained the same.

## 5. Main difference

- **Merge** is useful when I want to preserve the complete branch history and show where branches were joined.
- **Rebase** is useful for updating a private feature branch and creating a cleaner, linear history.
- I should avoid rebasing commits that have already been shared with others because changing commit hashes can disrupt other people's work.

---
