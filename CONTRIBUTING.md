## Contribution Guide

If you've found a small bug in cluster-flag, the most simple approach is to raise an issue [here](https://github.com/dashee87/cluster-flag/issues) and I'll take it from there.

If you want to fix a bug yourself, add new flags (preferably with a star) or generally improve the project, then please follow these guidelines (adapted from the corresponding [scikit-learn page](https://github.com/scikit-learn/scikit-learn/blob/master/CONTRIBUTING.md)):


* Fork the [project repository](https://github.com/dashee87/cluster-flag/)
   by clicking on the 'Fork' button near the top right of the page. This creates
   a copy of the code under your GitHub user account.

* If bash and git aren't really your thing, generate your python files locally and simply drop them into your forked repositry page (making sure that they're **not** added to your master branch). You can now jump to the final bullet point.

* Alternatively, clone your fork of the cluster-flag from your GitHub account to your local disk:

   ```bash
   $ git clone git@github.com:YourLogin/cluster-flag.git
   $ cd cluster-flag
   ```

* Create a ``feature`` branch to hold your development changes:

   ```bash
   $ git checkout -b my-feature
   ```

   Always use a ``feature`` branch. It's good practice to never work on the ``master`` branch!

* Develop the feature on your feature branch. Add changed files using ``git add`` and then ``git commit`` files:

   ```bash
   $ git add modified_files
   $ git commit
   ```

   to record your changes in Git, then push the changes to your GitHub account with:

   ```bash
   $ git push -u origin my-feature
   ```


* Go to the GitHub web page of your forked repo.
Click the 'Pull request' button to send your changes to me. I'll look over the code and accept the changes if it improves the project.

All contributions (however minor) are welcome!