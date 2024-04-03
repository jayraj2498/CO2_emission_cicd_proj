## End to End MAchine Learning Project 


#### we will track our data by using DVC :- data version control 
- we will track our data store in our artifacts folder 
- usually we have to big data so we can put them in CI or it is not posible we store our bigdata in our repository  
- we have to control that data so we track our file (artifact file ) by using DVC 
- as git has command DVC also have the command 
    -- to initiallize dvc --> dvc init  
       you get .dvc folder and .devcignore file -> in that you get more folder we will  commit it our main git tht'y 
- inside .dvc folder our data tracking happend  
- .devcignore inside 

- first we have to untrack artifacts folder file for next to track it y dvc 
- dvc add artifacts/data.csv  we run these 
- we get file 2 file in artifacts folder data.csv.dvc  , .gitignore 
- file looks like 
    outs:
- md5: 6206fc08bd4965cee784139be0b4640d
  size: 318565
  hash: md5
  path: data.csv

- we send  data.csv.dvc  to git  to track not our full data.csv file 
- we track data by-- >  dvc file    , data configration file --> github 
- incase if you have big data you put it into cloud that configraion info track by git 


