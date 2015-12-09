# Google Docs LaTeX

Google Docs LaTeX is a small helper written in Python and BASH shell script to automate the process of retrieving Google Docs containing TeX and BibTeX documents and compile them. When paired with the Google Drive app for Windows and Mac, the resulting PDF will be automatically synchronized to the source directory for viewing by anyone with access to the project directory. Google Drive LaTeX is licensed under the GNU General Public License version 3, or any future version at your discretion. See COPYING.md for details.

## Prerequisites

You must have an appropriate TeX and BibTeX compilers, Python 2.7, pip, and virtualenv installed on your machine. You must also have the Google Drive sync client if you need access to images and other media for `\includegraphics` or `\input` commands.

## Installing

Installing the package is easy. One must first create a virtual environment to manage the package requirements. The compile.sh script expects the virtualenv to exist in `~/.gdrive_env`, so if you create the virtualenv in a different location ___you will need to adjust the path in compile.sh___.

```shell
$ virtualenv ~/.gdrive_env
$ source ~/.gdrive_env/bin/activate
$ pip install -r requirements.txt
$ python setup.py install
```

## Running

There is a `compile.sh` file that is responsible for retrieving the LaTeX and BibTeX files from Google Docs and compiling them. The files are identified by the variable `PROJECT`, which is used to construct `PROJECT.tex` and `PROJECT.bib` document titles.

```shell
$ PROJECT="paper" ./compile.sh
```

To have the project name and directory persist for all compilations, change the two lines in `compile.sh` that set the `PROJECT_DIR` and `PROJECT` environment variables.

## Cron Job Configuration

First, copy the `compile.sh` script to the Google Drive directory synchronized to the computer that will be responsible for running the cron job.

Second, in a shell, enter `crontab -e` to edit your crontab. Add the following line, adjusting to compile at the desired interval and to change the directory into the appropriate project path.

```shell
*/10 * * * * bash -c 'cd ~/Google Drive/path/to/project/directory && chmod +x compile.sh && ./compile.sh'
```

## Advanced

Additional things that can be adjusted:

* PROJECT - Name of the project, used to identify the TeX and BibTeX documents on Google Docs.
* PROJECT_DIR - Optional, directory name to locate the PROJECT files. Useful for when the project name is ambiguous, such as paper.tex.
* TEX - Optional, TeX engine used to compile the TeX document. Defaults to xelatex.
* BIBTEX - Optional, BibTeX engine used to compile the BibTeX document. Defaults to bibtex.

## Using a Build System

If you have a more complex TeX project that requires more than the default configuration of latex, bibtex, latex, latex, you can also swap out the behavior for a more robust build system, such as a Makefile. Simply replace the calls to TEX and BIBTEX in `compile.sh` with a call to make.

## Suggested Best Practices

The formatting in Google Docs is transient for the purposes of TeX compilation, so it is often useful to change headings like `\section` and `\subsection` to use the Header formatting options in Google Docs. This makes them easier to identify in the source.

### Table of contents

If you use the Header formatting options in Google Docs, you can generate a table of contents within the Google Doc to quickly link to the different sections of the paper. Add `\usepackage{verbatim}` and place the TOC between `\begin{comment}` and `\end{comment}` so that it won't get compiled into the PDF.

### Images

Using the same technique as the Table of Contents, you can also embed images in the Google Doc within `\begin{comment}` and `\end{comment}` commands to preview the images in relation to the TeX. Arrangement will differ to the final product, but it does provide a way to quickly get a sense of how the ordering of the figures will appear.

### Docs comments

If you use comments to identify TODOs or have discussion about the TeX in Google Docs, it is best to ensure that the comment ends not directly after a closing curly brace. This is because the text version of a Google Doc retrieved by this script translates comments into identifiers such as [a], [b], ... and at the end of the document includes the text of the comment, "[a] Please fix this!" Since LaTeX uses square brackets to indicate optional parameters to commands, ending a comment immediately after a curley brace can result in the comment identifier being erroneously passed as an optional argument. One trick is that if the comment ends the line is to ensure that the text the comment is applied to ends with a percent (%) sign, which is the TeX comment character.

### TeX comments

It is often useful to quickly identify comments in the TeX source. Because Google Docs isn't a TeX editor, it does not understand things like TeX comments. Generally, it is useful to other authors that when you comment out TeX, either using the percent sign (%) or `\begin{comment}` and `\end{comment}` commands, to change the text color of the associated block to some salient color, such as red.
