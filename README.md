<img width="1917" height="1028" alt="image" src="https://github.com/user-attachments/assets/3f8b2a6a-6751-4140-b2d2-d3e01b64ad6c" /># i-count - Docker Project
in this project i put my docker skills to the test and containerised and deployed a flask app using redis 
i decied to make a local host website with a visitor counter and have seperate routes for each page 
at then end of the link 
/ = should show the main page
count/ = shout show the visitor count page 
<img width="1918" height="1033" alt="Screenshot 2025-08-09 234413" src="https://github.com/user-attachments/assets/767f705c-d451-4aa4-ae1f-423c39809060" />
<img width="1919" height="1029" alt="Screenshot 2025-08-09 234403" src="https://github.com/user-attachments/assets/8452f952-1c18-4d2d-ab8c-c29a5d0bfca2" />

first i created my 3 necesarry files docker file, docker compose and app.py 
<img width="163" height="68" alt="image" src="https://github.com/user-attachments/assets/15987638-2f02-41ca-9021-c40000118333" />
next i decided i wanted to style my pages so i added html files for them with a templates directory 
<img width="162" height="86" alt="image" src="https://github.com/user-attachments/assets/afd01b86-bf55-4205-b1cd-d0d856a53ad6" />

i then added the code for my flask app <img width="716" height="641" alt="image" src="https://github.com/user-attachments/assets/7e98be3d-7746-4858-8db5-a1454f24c9de" />

after that i added the html needed to style my pages 
<img width="1397" height="1007" alt="image" src="https://github.com/user-attachments/assets/51e47249-c12d-4c27-9084-e7e11577fd90" />
<img width="401" height="194" alt="image" src="https://github.com/user-attachments/assets/6cc23dcc-f02c-4dab-a2f2-5d32834f5084" />
<img width="638" height="210" alt="image" src="https://github.com/user-attachments/assets/63375824-92a0-42d1-9e38-19ae7043c2b9" />

once that was complete i wanted to reinforce what io have learned about docker 
so once that was completed i first ran my app using the python command to check if it was working 
<img width="603" height="161" alt="Screenshot 2025-08-10 015137" src="https://github.com/user-attachments/assets/bd19658f-7890-455c-9b11-ef34a67b4e7f" />

after that i added code into my docker file in order to create an image out of my web app so that i could containerise it 
<img width="622" height="355" alt="image" src="https://github.com/user-attachments/assets/080ce2a3-3c05-498a-968f-b81b947c2e13" />

next i built the image and made it into a container .
command i used to build 
docker build -t icount-test . 
the build command creats and image, -t tags it with a name, . specifies this directory
<img width="616" height="251" alt="image" src="https://github.com/user-attachments/assets/acd89586-2a0f-4eda-b76a-474892395755" />
<img width="965" height="345" alt="image" src="https://github.com/user-attachments/assets/bfd15ef3-56dc-42ce-b684-9016ec8f772d" />

command i used to containerise and run 
the run command runs the image as a cointainer -d means to deattach it to run as a container  --name sets the name -p sets the port then at the end you choose your image 
docker run -d --name icount-test -p 5003:5003 icount-test 
<img width="1149" height="136" alt="image" src="https://github.com/user-attachments/assets/825a43ac-b9ec-4aa0-9536-ac536b77a535" />

final product 
<img width="1914" height="1031" alt="image" src="https://github.com/user-attachments/assets/fbf015e0-1ade-459a-ae34-a547cd769c93" />

The next thing i did was connect this container with a redis image  then run on a custom network so that they both can intereract with each other 
so i created my network 
<img width="617" height="295" alt="image" src="https://github.com/user-attachments/assets/7fb5d824-4d99-413c-b940-432315b4d812" />

Then i ran my docker image on the customer network - --network specifies the network the container should run on 
<img width="612" height="169" alt="image" src="https://github.com/user-attachments/assets/fad11dd4-7dd9-40de-aa87-4dbd78df9828" />

next was to make a redis data base image then run it on the same network
normally redis would install how ever it was already installed foir me 
<img width="612" height="268" alt="image" src="https://github.com/user-attachments/assets/b8bdfede-e92e-4156-a2d1-640855a4e5cf" />
<img width="956" height="376" alt="image" src="https://github.com/user-attachments/assets/9b28b051-491e-4780-8eab-327b23907bf7" />

Now heres where i ran into an issue 
my app was working but the vitis counter was not even though my redis data base was connected to the customer network and running 
<img width="691" height="713" alt="image" src="https://github.com/user-attachments/assets/d88a7e4f-7f4e-4912-a6a5-673c3bc7b721" />

At one point, my site loaded fine, but the visit counter refused to go up. Redis (the database) was running and connected to my custom Docker network, so I thought it should work.

After a bit of digging, I found the problem — my Flask app didn’t actually know where Redis was. Inside Docker, localhost means “this container,” not another one. Since I hadn’t told Flask the Redis container’s name, it kept looking in the wrong place.

How I fixed it:
i first checked if both contaioners were on the same network using the docker network inspact command as i knew it couldnt be a container issue since they were up and running 
and the result showed they was 
<img width="592" height="289" alt="image" src="https://github.com/user-attachments/assets/f5f1d536-20c1-4cba-a06f-e53e8116edc0" />

next i searched the internet to see if i could find some resolution 
while i dint find my exact answer i tried somethings i found on this site 
https://www.dragonflydb.io/error-solutions/could-not-connect-to-redis-at-127-0-0-1-6379-connection-refused-docker
such as using docker inspect redis - to search for any errors, exit code ect to my suprise everything was running
another thing i tried was docker logs redis - while it said there was no conf file i didnt think that was the issue as it was ready to accept connections
<img width="615" height="224" alt="image" src="https://github.com/user-attachments/assets/63060408-6cc8-4cb4-9c59-6ad0bc08d158" />

i then tried to change the port to match my main page port but it did not work as the port was being used 
so i was stuck and unsure what to do so then i asked for help from one of my peers and we tried to debug for a while 

Turns out in my run command for my flask image i was missing the REDIS_HOST environmental veriable from my run command as this is needed for redis to connect a database to my flask app i found this through debugging help and shows that its okay to ask people for help when you are stuck
<img width="646" height="278" alt="image" src="https://github.com/user-attachments/assets/150c6ba1-119e-4c08-8bd0-dfa41a93a949" />
<img width="504" height="157" alt="image" src="https://github.com/user-attachments/assets/2430a9f5-3aea-4197-9971-4c8b0b8851cf" />
and as you can see it works
<img width="578" height="485" alt="image" src="https://github.com/user-attachments/assets/9e2fc3e9-4205-4484-8667-7ec09ff61ac7" />

finally it came to us9ing docker compose so i wouldnt have to make a custom network and connect both images everytime 
it was pretty simple to make 
<img width="724" height="499" alt="image" src="https://github.com/user-attachments/assets/b98528dd-1411-4372-869c-425f21440e14" />
once created all i do is docker compose up 
<img width="396" height="106" alt="Screenshot 2025-08-10 035240" src="https://github.com/user-attachments/assets/3712224a-0b34-4ffa-a201-5d3f76afcdd9" />

and here is the final result 
<img width="1917" height="1028" alt="Screenshot 2025-08-10 035352" src="https://github.com/user-attachments/assets/1249ec41-46c2-4257-8b2f-2ff998ff41eb" />

if i had to say this project really went well as i reenforced my knowledge on docker and was able to deploy an app with containerisation 

plans for the future:
scale with nginx image 
deploy live and push to amazon ecr 


