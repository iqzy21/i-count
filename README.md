# i-count: Flask Redis Containerisation Project

**Project Overview:** A hands-on containerisation project demonstrating multi-service Docker deployment using Flask web application with Redis database integration, custom networking, and Docker Compose orchestration.

<img width="1917" height="1028" alt="Screenshot 2025-08-10 035352" src="https://github.com/user-attachments/assets/01396dce-053f-4289-ab87-03d8870c1f52" />


---

## 🎯 Project Objectives

- Containerise a Flask web application using Docker
- Implement Redis database integration for visitor counting functionality
- Configure custom Docker networking for inter-container communication
- Utilise Docker Compose for multi-service orchestration
- Apply systematic troubleshooting techniques for container connectivity issues

---

## 🏗️ Application Architecture

### Core Functionality
In this project I put my Docker skills to the test and containerised and deployed a Flask app using Redis. I decided to make a localhost website with a visitor counter and have separate routes for each page at the end of the link:

- **`/`** - Main page display
- **`/count`** - Visitor count tracking page

![Main Page](https://github.com/user-attachments/assets/767f705c-d451-4aa4-ae1f-423c39809060)
![Count Page](https://github.com/user-attachments/assets/8452f952-1c18-4d2d-ab8c-c29a5d0bfca2)

---

## 🚀 Implementation Process

### Phase 1: Project Structure Setup

First I created my 3 necessary files: Dockerfile, Docker Compose and app.py

![Initial File Structure](https://github.com/user-attachments/assets/15987638-2f02-41ca-9021-c40000118333)

Next I decided I wanted to style my pages so I added HTML files for them with a templates directory

![Enhanced File Structure](https://github.com/user-attachments/assets/afd01b86-bf55-4205-b1cd-d0d856a53ad6)

### Phase 2: Application Development

#### Flask Application Code
I then added the code for my Flask app

![Flask Application Code](https://github.com/user-attachments/assets/7e98be3d-7746-4858-8db5-a1454f24c9de)

#### HTML Template Development
After that I added the HTML needed to style my pages

![HTML Templates](https://github.com/user-attachments/assets/51e47249-c12d-4c27-9084-e7e11577fd90)

![Main Page Template](https://github.com/user-attachments/assets/6cc23dcc-f02c-4dab-a2f2-5d32834f5084)

![Count Page Template](https://github.com/user-attachments/assets/63375824-92a0-42d1-9e38-19ae7043c2b9)

### Phase 3: Local Testing & Validation

Once that was complete I wanted to reinforce what I have learnt about Docker so once that was completed I first ran my app using the Python command to check if it was working

![Local Testing](https://github.com/user-attachments/assets/bd19658f-7890-455c-9b11-ef34a67b4e7f)

---

## 🐳 Containerisation Implementation

### Phase 4: Dockerfile Configuration

After that I added code into my Dockerfile in order to create an image out of my web app so that I could containerise it

![Dockerfile Configuration](https://github.com/user-attachments/assets/080ce2a3-3c05-498a-968f-b81b947c2e13)

### Phase 5: Image Build Process

Next I built the image and made it into a container.

**Command used to build:**
```bash
docker build -t icount-test .
```
*The build command creates an image, -t tags it with a name, . specifies this directory*

![Build Process](https://github.com/user-attachments/assets/acd89586-2a0f-4eda-b76a-474892395755)

![Build Completion](https://github.com/user-attachments/assets/bfd15ef3-56dc-42ce-b684-9016ec8f772d)

### Phase 6: Container Deployment

**Command used to containerise and run:**
```bash
docker run -d --name icount-test -p 5003:5003 icount-test
```
*The run command runs the image as a container -d means to detach it to run as a container --name sets the name -p sets the port then at the end you choose your image*

![Container Deployment](https://github.com/user-attachments/assets/825a43ac-b9ec-4aa0-9536-ac536b77a535)

**Initial containerised result:**

![Initial Container Result](https://github.com/user-attachments/assets/fbf015e0-1ade-459a-ae34-a547cd769c93)

---

## 🔗 Multi-Service Integration

### Phase 7: Custom Network Configuration

The next thing I did was connect this container with a Redis image then run on a custom network so that they both can interact with each other so I created my network

![Network Creation](https://github.com/user-attachments/assets/7fb5d824-4d99-413c-b940-432315b4d812)

Then I ran my Docker image on the customer network - --network specifies the network the container should run on

![Network Assignment](https://github.com/user-attachments/assets/fad11dd4-7dd9-40de-aa87-4dbd78df9828)

### Phase 8: Redis Database Integration

Next was to make a Redis database image then run it on the same network normally Redis would install however it was already installed for me

![Redis Setup](https://github.com/user-attachments/assets/b8bdfede-e92e-4156-a2d1-640855a4e5cf)

![Redis Container Running](https://github.com/user-attachments/assets/9b28b051-491e-4780-8eab-327b23907bf7)

---

## 🔧 Problem Analysis & Resolution

### Issue Identification

Now here's where I ran into an issue - my app was working but the visit counter was not even though my Redis database was connected to the customer network and running

![Problem Identification](https://github.com/user-attachments/assets/d88a7e4f-7f4e-4912-a6a5-673c3bc7b721)

### Root Cause Analysis

At one point, my site loaded fine, but the visit counter refused to go up. Redis (the database) was running and connected to my custom Docker network, so I thought it should work.

After a bit of digging, I found the problem — my Flask app didn't actually know where Redis was. Inside Docker, localhost means "this container," not another one. Since I hadn't told Flask the Redis container's name, it kept looking in the wrong place.

### Systematic Troubleshooting Approach

**How I fixed it:**

1. **Network Verification:** I first checked if both containers were on the same network using the docker network inspect command as I knew it couldn't be a container issue since they were up and running and the result showed they were

![Network Inspection](https://github.com/user-attachments/assets/f5f1d536-20c1-4cba-a06f-e53e8116edc0)

2. **Research & Documentation Review:** Next I searched the internet to see if I could find some resolution whilst I didn't find my exact answer I tried some things I found on this site: https://www.dragonflydb.io/error-solutions/could-not-connect-to-redis-at-127-0-0-1-6379-connection-refused-docker

3. **Container Diagnostics:** Such as using `docker inspect redis` - to search for any errors, exit code etc to my surprise everything was running another thing I tried was `docker logs redis` - whilst it said there was no conf file I didn't think that was the issue as it was ready to accept connections

![Redis Logs](https://github.com/user-attachments/assets/63060408-6cc8-4cb4-9c59-6ad0bc08d158)

4. **Collaborative Problem Solving:** I then tried to change the port to match my main page port but it did not work as the port was being used so I was stuck and unsure what to do so then I asked for help from one of my peers and we tried to debug for a whilst

### Solution Implementation

**Root Cause Discovery:** Turns out in my run command for my Flask image I was missing the REDIS_HOST environmental variable from my run command as this is needed for Redis to connect a database to my Flask app I found this through debugging help and shows that it's okay to ask people for help when you are stuck

![Environment Variable Fix](https://github.com/user-attachments/assets/150c6ba1-119e-4c08-8bd0-dfa41a93a949)

![Working Solution](https://github.com/user-attachments/assets/2430a9f5-3aea-4197-9971-4c8b0b8851cf)

**Verification:** And as you can see it works

![Solution Verification](https://github.com/user-attachments/assets/9e2fc3e9-4205-4484-8667-7ec09ff61ac7)

---

## 📦 Docker Compose Implementation

### Phase 9: Service Orchestration

Finally it came to using Docker Compose so I wouldn't have to make a custom network and connect both images every time - it was pretty simple to make

![Docker Compose Configuration](https://github.com/user-attachments/assets/b98528dd-1411-4372-869c-425f21440e14)

Once created all I do is `docker compose up`

![Docker Compose Execution](https://github.com/user-attachments/assets/3712224a-0b34-4ffa-a201-5d3f76afcdd9)

**Final Result:**

![Final Project Result](https://github.com/user-attachments/assets/1249ec41-46c2-4257-8b2f-2ff998ff41eb)

---

## 📊 Project Outcomes & Technical Skills Demonstrated

### Core Competencies Applied:
- **Docker Containerisation** - Image creation, container management, and multi-service deployment
- **Flask Web Development** - Python web application with routing and templating
- **Redis Database Integration** - NoSQL database implementation for persistent data storage
- **Docker Networking** - Custom network creation and container communication
- **Docker Compose** - Multi-service orchestration and environment management
- **Systematic Troubleshooting** - Methodical problem identification and resolution
- **Environment Configuration** - Container environment variables and service discovery

### Key Technical Insights:
1. **Container Communication** - Understanding that localhost within containers refers to the container itself, not other containers
2. **Environment Variables** - Critical importance of proper environment configuration for inter-service communication
3. **Network Isolation** - Docker networks provide isolation whilst enabling controlled communication
4. **Service Discovery** - Container names serve as hostnames within Docker networks
5. **Orchestration Benefits** - Docker Compose simplifies multi-service deployment and management

### Problem-Solving Methodology Demonstrated:
1. **Systematic Verification** - Network inspection and service status validation
2. **Research & Documentation** - Leveraging external resources for problem resolution
3. **Collaborative Debugging** - Effective peer collaboration for complex issues
4. **Root Cause Analysis** - Identifying underlying configuration issues
5. **Solution Validation** - Confirming fixes through testing and verification

---

## 🚀 Future Enhancements

**Plans for the future:**
- Scale with Nginx image
- Deploy live and push to Amazon ECR

---

## 💡 Business Value & Real-World Applications

This project demonstrates practical skills directly applicable to:
- **DevOps Engineering** - Container orchestration and multi-service deployment

**Project Reflection:** If I had to say this project really went well as I reinforced my knowledge on Docker and was able to deploy an app with containerisation.

The systematic approach to troubleshooting and the collaborative problem-solving demonstrated here reflects industry-standard practices for production environment management and complex system integration.
