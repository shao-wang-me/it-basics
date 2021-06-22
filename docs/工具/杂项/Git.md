# Git

Git 是一个版本控制系统，对纯文本（代码等）有很好的支持。

## Git 是一个内容寻址文件系统

在 Git 里（`.git` 文件夹，对象（文件、提交等）都是 hash 并存储在以 hash 索引的文件夹结构里，任何相同内容的对象都只存在一份。因此你可以查询某文件是不是在 Git 中，如果在，在哪里。

## 更新 Windows 上 的 Git

2.16.1 以后版本的 Git，直接 `git update-git-for-windows`。

参考：<https://stackoverflow.com/questions/13790592/how-to-upgrade-git-on-windows-to-the-latest-version>

## 检出一个标签（tag）

`git checkout tags/<tag_name>` 或者 `git checkout <tag_name>`，推荐第一个因为可能有同名标签。

## Git Merge Base

```shell
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

## Git Rebase

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

## Mail map

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

## 其它

### Git 统计

[git-quick-stats](https://github.com/arzzen/git-quick-stats)

```shell
# Install
apt install git-quick-stats
brew install git-quick-stats

# Statistics
export _GIT_SINCE="2021-01-16"
git quick-stats --detailed-git-stats
```
