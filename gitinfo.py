import urllib2
from BeautifulSoup import BeautifulSoup
import sys
import argparse
import re

def gitinfo():
    parser = argparse.ArgumentParser()
    parser.add_argument("author",help="Name of the author of the repo")
    parser.add_argument("reponame",help="Name of repo")

    args = parser.parse_args()

    repository = "https://github.com/%s/%s/" % (args.author,args.reponame)

    print("Opening Repo!")

    try : urllib2.urlopen(repository)
    except urllib2.HTTPError:
        print "No such repository"
        sys.exit(1)

    print("Extracting Info!")

    soup = BeautifulSoup(urllib2.urlopen(repository).read())

    s=soup.find('a',{ "class" : "social-count js-social-count" })

    stars = s.contents[0].replace(" ",'')



    fork=soup.find('a',{ "class" : "social-count" })
    forks = fork.contents[0].replace(" ",'')

    br = soup.findAll("span",{'class':'num'})
    commits =str(br[0]).split()[5]
    branches = str(br[1]).split()[5]
    releases = str(br[2]).split()[5]
    contributors = str(br[3]).split()[5]

    if contributors == "</span>":
        contributors = contributors.replace("</span>","0")

    print("Opening Pulse Page!")

    rw = urllib2.urlopen(repository+"pulse").read()

    soup = BeautifulSoup(rw)
    b = soup.findAll("span",{'class':'num'})

    merged = str(b[2]).split()[5]
    proposed = str(b[3]).split()[5]
    closed = str(b[4]).split()[5]
    new = str(b[5]).split()[5]

<<<<<<< HEAD:GitInfo.py






    print("\nName : %s" %repository.split('/')[4])
    print("Author : %s" % repository.split('/')[3])
=======
    print("\nName : %s" % args.reponame)
    print("Author : %s" % args.author)
>>>>>>> origin/master:gitinfo.py

    print("\nThis repository has been starred %s time(s)\n"% str(stars.replace("\n",'')))
    print("%s Person(s) have forked this repo\n"% str(forks.replace("\n",'')))
    print("\n")
    print("This Repository has ::\n"
            "%s Merged Pull Requests\n"
            "%s Proposed Pull Requests\n"
            "%s Closed Issues\n"
            "%s New Issues\n"%(merged,proposed,closed,new))
    print('\n')
    print("This Repository has :: \n"
          "%s Contributor(s)\n"
          "%s Branches\n"
          "%s Commits\n"
          "%s Releases\n"%(contributors,branches,commits,releases))
    print("Finding Latest Issue\n")

    GitIssues(args.author,args.reponame)


def GitIssues(author,repo):

    issues = urllib2.urlopen("https://github.com/%s/%s/issues/" %(author,repo)).read()
    soup = BeautifulSoup(issues)

    try : soup.findAll("span",{'class':'list-group-item-number'})[0]
    except IndexError: print("ERROR! This Repo has 0 issues.")
    else:
        h = (str(soup.findAll("span",{'class':'list-group-item-number'})[0]))

        valid = r'<span(.*?)>(.*)</span>'
        num = (re.match(valid,h).group(2)).replace('#',"")

        fin = urllib2.urlopen("https://github.com/%s/%s/issues/%s" %(author,repo,num)).read()
        title = BeautifulSoup(fin)

        name = str(title.find("a",{'class':'author'}))
        reg = r'<a.*?>(.*)</a>'
        issueaut = (re.match(reg,name).group(1))


        for d in title.findAll("title"):
            issuename = (d.contents[0])


        print("Issue Title = %s\n" %issuename[:-6])
        print("Issue Author = %s\n" % issueaut)







if __name__ == '__main__':
    gitinfo()
