__author__ = 'Hassaan'
import urllib
from BeautifulSoup import BeautifulSoup
import DownloadSc
import sys
import datetime


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

def Write2File(repository):

    now = datetime.datetime.now()
    file = open("%s-%s.txt" %(now.date(),repository.split('/')[4]),'w+')

    r = urllib.urlopen(repository).read()

    soup = BeautifulSoup(r)

    star=soup.find('a',{ "class" : "social-count js-social-count" })
    stars = star.contents[0].replace(" ",'')

    fork=soup.find('a',{ "class" : "social-count" })
    forks = fork.contents[0].replace(" ",'')

    br = soup.findAll("span",{'class':'num'})
    commits =str(br[0]).split()[5]
    branches = str(br[1]).split()[5]
    releases = str(br[2]).split()[5]
    contributors = str(br[3]).split()[5]

    if contributors == "</span>":
        contributors = contributors.replace("</span>","0")

    rw = urllib.urlopen(repository+"pulse").read()

    soup = BeautifulSoup(rw)
    b = soup.findAll("span",{'class':'num'})


    merged = str(b[2]).split()[5]
    proposed = str(b[3]).split()[5]
    closed = str(b[4]).split()[5]
    new = str(b[5]).split()[5]





    file.write("Name : %s\n" %repository.split('/')[4])
    file.write("Author : %s\n" % repository.split('/')[3] )
    file.write("\n")
    file.write("\n")
    file.write("This repository has been starred %s time(s)\n"% str(stars.replace("\n",'')))
    file.write("%s Person(s) have forked this repo\n"% str(forks.replace("\n",'')))
    file.write("\n")
    file.write("\n")

    file.write("This Repository has :: \n"
          "%s Contributor(s)\n"
          "%s Branches\n"
          "%s Commits\n"
          "%s Releases\n"%(contributors,branches,commits,releases))

    file.write("\n")
    file.write("\n")

    file.write("This Repository has ::\n"
            "%s Merged Pull Requests\n"
            "%s Proposed Pull Requests\n"
            "%s Closed Issues\n"
            "%s New Issues\n"%(merged,proposed,closed,new))
    file.close()
















if __name__ == '__main__':

    url =raw_input("Please enter Valid GitHub repo URL\n")
    if url[-1] != '/':
        url = url+'/'#add last backslash

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
          "exit : Exit\n"
          "text : Write all info to a text file\n" )

    choice = raw_input("Please enter your choice :")

    if choice == "forks":
        GetForks(url)
        choice = raw_input("Please enter your choice :")

    if choice =="text":
        Write2File(url)
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







