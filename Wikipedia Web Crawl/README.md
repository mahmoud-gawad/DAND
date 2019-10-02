# Case Study: Wikipedia Web Crawl

In this mini-project, it is asked to write a small program that would go to Wikipedia, select a random topic, and follow every first link in the article to see if, eventually, the program would reach the article "Philosophy".

## How the Crawler Works

The program would make a set of steps to reach the final output, listed as:

1. Open an article
2. Find the first link in the article
3. Follow the link
4. Repeat the process until we reach the Philosophy article, or get stuck in an article cycle

## The Program

The pgoram itself is fairly simple. It consists of two functions: `continue_crawl` which controls the main `while` loop that follows the links, and `find_first_link` which for each article, tries to find the first article link in that article.

## Implementation Details

Some of the implementation decisions came after some iterations. As an example, the first version of the code looked only for the first link in the first paragraph, but some article pages have a hidden first paragraph that shows inside the parser and hence return no links, while other pages have different links listed before an article link (footnotes, pronunciations, etc.).

Another thing I needed was a data structure to hold a record of all the articles visited before, to display them when executing the program so one can follow the same path manually if wanted. Also the program can't keep running indefinitely, so there had to be a maximum bound to the number of articles the program needs to check before terminating the operation.

These details had to be taken care of, I created some specific cases that ensure getting only an article link from each page the program visits, and created a list, named `article_chain` that holds the record for all the visited articles and is printed one by one when the program runs, and a `limit` variable that indicates the maximum articles count. And of course, there had to be a small delay, so that we wouldn't flood Wikipedia's servers with requests and risk getting ourselves blocked, or worse.

## Output

The final output would be one of 4 cases:

* The program reaches the Philosophy article page, then a message indicating that will appear.
* Or the program exceedes the maximum number of requests, then a message shows that.
* Or the program reaches a page that has no links, in such case the program would stop with a message indicating the status.
* Finally, the program could find itself in a loop, when the article chain keeps repeating itself, then the program stops and prints a message indicating that.

In each case, the article chain leading to one of the cases above is printed before the message that tells us what the final status of the program is.
