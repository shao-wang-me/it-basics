# Git

1. Why is Git a content-addressable file system?

   Because in `.git` folder, objects (files, commits, etc.) are hashed and stored a directory structure indexed by the hash. There is only one copy for any objects with the same content (thus the same hash).

   There might be some mechanism to handle hash conflicts but conceptually things are addressed by the content.

1. How to update Git for Windows?

   Since probably version 2.16.1, use `git update-git-for-windows`.

   (https://stackoverflow.com/questions/13790592/how-to-upgrade-git-on-windows-to-the-latest-version)

1. How to checkout a tag?

   `git checkout tags/<tag_name>` or `git checkout <tag_name>`. The first one is recommended because there might be a branch with the same name.

1. How to get the last common ancestor of branches/commits?

   ```
   git merge-base --all <commit_1> <commit_2>
   git merge-base --all --octopus <commit_1> <commit_2> <commit_3> ...
   ```

   Add `--all` to list all possible ancestors (equally good).

   If you have more than two commits, you can add `----octopus` otherwise it is the ancestor of the first commit, and a hypothetical commit which is a merge of all other commits.

   Examples:

   ```
            o---o---o---B
           /
   ---o---1---o---o---o---A
   git merge-base A B = 1

          o---o---o---o---C
         /
        /   o---o---o---B
       /   /
   ---2---1---o---o---o---A
   git merge-base --octopus A B C = 2

   ---1---o---A
       \ /
        X
       / \
   ---2---o---o---B
   git merge-base --all A B = 1 2
   ```

1. What is `git rebase`?

   `git rebase` essentially replays the changes of commits.
   
   `git rebase base change` will first switch to `change`, replay changes in `change` after the merge base of `change` and `base` onto `base` and commit these new derived commits (hashes are different because the contents are different) in `change`.

   `git rebase --onto new_base base change` is similar, except that it replays the changes onto `new_base` instead of `base`.

   Examples:

   ```
         A---B---C topic
        /
   D---E---F---G master
   git rebase master topic =>
                 A'--B'--C' topic
                /
   D---E---F---G master

   o---o---o---o---o  master
        \
         o---o---o---o---o  next
                          \
                           o---o---o  topic
   git rebase --onto master next topic =>
   o---o---o---o---o  master
       |            \
       |             o'--o'--o'  topic
        \
         o---o---o---o---o  next
   ```

   If there is any conflict, it will enter the interactive rebase mode. You can `git rebase --abort`. Or you can resolve conflicts, `git add` them and `git rebase --contibue`, it will finish the rebase or let you resolve remaining conflicts.

   It seems that the default interactive rebase resolves two commits each round but you can `git rebase --edit-todo` to adjust the range.

1. What is `.mailmap`?

   In `.mailmap` you can specify canonical names and emails to be displayed in `git log` and other places. You can use this to handle wrong names or emails in commits.

   ```
   # Based on <commit@email>
   Display Name <commit@email>  # Replace name
   <display@email> <commit@email>  # Replace email
   Display Name <display@email> <commit@email>  # Replace both

   # Based on both <Commit Name> and <commit@email>
   Display Name <Commit Name> <commit@email>  # Replace name
   <display@email> Commit Name <commit@email>  # Replace email
   Display Name <display@email> Commit Name <commit@email>  # Replace both
   ```
