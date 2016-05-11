Why Non-Linear Git?
    What if we want to try something new and crazy without breaking code that we''ve already written?

    What if we want to work on two different features simultaneously?

    What if we want multiple people to work on the same code without stepping on each other''s toes?

Branches: allow for non-linear commits

Branch Commands
    git branch --> * master (star means thats the branch we are currently on)
        List available branches
    git branch [my_branch]
        Create a new branch called "my_branch" (from whatever branch you are currently on)
    git checkout [my_branch] --> Switched to branch 'experiment' (now commmits go here)
        Switch to branch "my_branch"
    git checkout -b [my_branch]
        Create and switch to branch "my_branch"
    git branch -d [my_branch]
        Delete branch "my_branch"

    HEAD - what branch you are currently on
        - when change to experiment branch, now HEAD, commit once creates new branch --> commit again, moves 1 more step ahead of master
        - go back to master (git checkout master) --> new commit creates new master branch version
        - go back to experiment branch (git checkout experiment) --> moves HEAD back to experiment

Branch Practice!
    Open the favorites.py file
    Create and checkout a new branch called experiment (git checkout -b experiment)
    Add another line of code at the end of the file printing out a favorite thing (echo "\nprint('bey')" >> favorites.py)
    Commit your change (hint: use git commit -am "msg" to add and commit at once!) (git commit -am "add new fav")
    checkout the master branch
    Add yet another line at the beginning of the file (echo -e "print('cheeseburgerbackpack')\n$(cat favorites.py)" > favorites.py)
    Commit your change (git commit -am "add first fav")
    Switch between the experiment and master branches (clicking on Sublime inbetween). See the file contents changing?

Undoing with Checkout: We can use checkout to switch not only to the commit named by a branch, but to any commit in order to "undo" our work.
    git checkout -b bugfix a16a49f

Detached Head: If you don''t create a new branch when checking out an old commit, you''ll enter detached HEAD state. You can''t commit from here, because there is no branch for that commit to be attached to!

Merging: We can merge two branches back together, producing a commit that contains the combined changes from both branches

    git merge [other_branch] --no-edit
        Merges changes from other_branch into the current branch.
    A new commit is created on the current branch containing the merged content.

Merging Practice
    Make sure you are on the master branch 
    (use git branch to check; the current branch has a *)
    Use git merge to merge the experiment branch into master branch.
    Remember to use the --no-edit flag so you don''t get dropped into vi! If you do, hit :q (colon then q) to flee.
    Check in Sublime that the file now contains both sets of changes!
    Once you''re satisfied, delete the experiment branch.

Merging Practice II
    You should be on the master branch.
    Create and checkout a new branch called danger
    On the danger branch, change the word "kittens" to "puppies". Remember to commit your change.
    checkout the master branch again.
    Change the word "kittens" to something else that is pleasant. commit your change.
    Use git merge to merge the danger branch into master branch (git merge danger --no-edit)
     
    Don''t panic!
        Auto-merging favorites.py
        CONFLICT (content): Merge conflict in favorites.py
        Automatic merge failed; fix conflicts and then commit the result.

Merge Conflicts
    A merge conflict is when two commits from different branches include different changes to the same code.
    Git does not know which version to keep, so makes you choose. 

    Merge conflicts must be resolved manually
    Conflicts are expected!

Resolving Conflicts
    In order to resolve a conflict, you need to edit the file (code) so that you pick which version to keep. 
    git will add "code" where you need to make a decision:

    <<<<<<< HEAD <--versions to pick from!

    # This is the code from the "local" version (the branch you merged INTO)
    # a.k.a the version from the HEAD commit

    print("I am a original!")
    print("I've got no strings to hold me down!")

    # it can be multiple lines

    ======= <--divider between versions

    # This is the code from the "remote" version (the branch you merged FROM)

    print("I think I'm a clone now...")

    >>>>>>> f292a3332aedc8df3e8e8cf22ca3debc214c6460 <--end conflict area

    once manually fix merge conflict, file still marked as merge conflict --> add/commit changes (commit concludes merge - can do git commit --no-edit)

Resolving Conflicts
Use git status to see which files have merge conflicts. Note that files may have more than one! 
 
Delete the <<<<<<< and ======= and >>>>>>> !! 
 
Once you''re satisfied that the conflicts are all resolved, add and commit your changes (the code you "modified" to resolve the conflict):
    git add .
    git commit --no-edit

Rebasing
    An alternative to merging.

    Rather than creating a new commit that is the "merger" of the two branches, takes the commits from one branch and tacks them on to the end of the other.
    http://www.wei-wang.com/ExplainGitWithD3/#
    
    This changes history.
    My advice: do not rebase

Remote Branches: Other linked repositories (remotes, like the one on Github that you cloned from) can simply be seen as different branches that happen to live on another machine.
   
    git branch -a
      danger
    * master
      remotes/origin/HEAD -> origin/master
      remotes/origin/master
      remotes/origin/other

Remote Branch Cmds:
    git branch -a
        List all branches (including remote ones)
    git fetch
        Import branches from remote into local repo
        Are still listed as "remote" branches that need to be merged
    git pull [remote branch]
        Shortcut for git fetch then git merge - take those commits and merge them into my commits
    git push [remote branch]
        Upload commits to remote 
        Essential has the remote branch merge (rebase) your changes.
    git push [remote] --all
        Push all branches

Collaboration: Multiple people''s local repositories can be linked to the same remote repository, allowing them to push and pull to the same central location.
Collaboration Practice
Person 1: edit the README.md file so it includes a message to your partner (be nice)
add and commit your change as usual.
 
Person 2: create a new file partner.py that prints a message to your partner (be nice)
add and commit as usual.
 
Person 1 should push their changes to Github
 
Then Person 2 should push their changes to Github
WHAT HAPPENED?!
Person 2: pull to merge in Person 1''s message
Both people should confirm the changes are local!
 
Person 2: push your changes to Github
 
Person 1: pull in Person 2''s message and merger
You both should now have up-to-date code!

Person 1: edit the partner.py file so that it prints a different message. Change the existing line of code.
add and commit your change as usual.
 
Person 2: edit the partner.py file so that it prints a different message. Change the existing line of code.
add and commit as usual.