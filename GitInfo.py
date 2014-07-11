__author__ = 'Hassaan'
import urllib
from BeautifulSoup import BeautifulSoup
import DownloadSc
import sys


def GetStars(repository):

    r = urllib.urlopen(repository).read()

    soup = BeautifulSoup(r)
    s=soup.find('a',{ "class" : "social-count js-social-count" })

    stars = s.contents[0].replace(" ",'')
    print("This repository has been starred %s time(s)")%stars.replace("\n",'')

def GetForks(repository):
    r = urllib.urlopen(repository)
    soup = BeautifulSoup(r)
    s=soup.find('a',{ "class" : "social-count" })
    forks = s.contents[0].replace(" ",'')

    print("%s Person(s) have forked this repo"% forks.replace("\n",''))


def GetSummary(repository):
    r = urllib.urlopen(repository)
    soup = BeautifulSoup(r)
    #s=soup.find('div',{ "class" : "capped-box overall-summary " })




    br = soup.findAll("span",{'class':'num'})
    commits =str(br[0]).split()[5]
    branches = str(br[1]).split()[5]
    releases = str(br[2]).split()[5]
    contributors = str(br[3]).split()[5]

    if contributors == "</span>":
        contributors = contributors.replace("</span>","0")

    print("This Repository has :: \n"
          "%s Contributor(s)\n"
          "%s Branches\n"
          "%s Commits\n"
          "%s Releases\n")%(contributors,branches,commits,releases)

def GetPulse(repository):

      r = urllib.urlopen(repository+"pulse").read()

      soup = BeautifulSoup(r)
      br = soup.findAll("span",{'class':'num'})


      merged = str(br[2]).split()[5]
      proposed = str(br[3]).split()[5]
      closed = str(br[4]).split()[5]
      new = str(br[5]).split()[5]
      print("This Repository has ::\n"
            "%s Merged Pull Requests\n"
            "%s Proposed Pull Requests\n"
            "%s Closed Issues\n"
            "%s New Issues\n")%(merged,proposed,closed,new)

def DownloadMaster(repository):

    Master = repository+"archive/master.zip"
    RepoName = repository.split('/')[4]+'-master'
    print(RepoName)

    DownloadSc.dl(Master,RepoName)
















if __name__ == '__main__':

    url =raw_input("Please enter Valid GitHub repo URL\n")
    print("Welcome to GitInfo.\n"
          "Please enter one of the following choices in the upcoming prompt\n"
          "\n"
          "\n"

          "forks : Get number of forks\n"
          "stars : Number of People who have starred this repo\n"
          "author : Name of author\n"
          "name : Name of repo\n"
          "summary : Get Branches,Commits,Releases & Contributors\n"
          "pulse : Get Number of Merged and Proposed Pull Requests and New and Closed Issues\n"
          "download: Downloads master branch as zip\n"
          "exit : Exit\n")

    choice = raw_input("Please enter your choice :")

    if choice == "forks":
        GetForks(url)
        choice = raw_input("Please enter your choice :")

    if choice == "stars":
        GetStars(url)
        choice = raw_input("Please enter your choice :")

    if choice == "author":
        print(url.split("/")[3])
        choice = raw_input("Please enter your choice :")

    if choice == "name":
        print(url.split('/')[4])
        choice = raw_input("Please enter your choice :")

    if choice == "summary":
        GetSummary(url)
        choice = raw_input("Please enter your choice :")

    if choice == "pulse":
        GetPulse(url)
        choice = raw_input("Please enter your choice :")

    if choice == "download":
        DownloadMaster(url)
        choice = raw_input("Please enter your choice :")

    if choice == 'exit': sys.exit(1)







