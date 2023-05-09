# Incoming Software Engineer Evaluation

In this repo are a series of coding questions and three quick programming exercises to evaluate where to best place you. Pull this repo and change the upstream branch from the MoonFall one to a personal public repository. A guide on how to do that can be found [here](https://devconnected.com/how-to-change-git-remote-origin/). Please fill out the info section on this page, the complete the quick answer questions below. 

There are also 3 programming challenges written in python 3. If you do not know python you can answer in detailed pseudocode or c++. Detailed descriptions for the tasks are in their folders README files. 

 - [C1: Game of Life](C1/README.md)
 - [C2: Matrix Operations](C2/README.md)
 - [C3: Calculator](C3/README.md)

When you are finished, push the code to your own repo and send the link to maxwildersmith@gmail.com.

---
## Info

Name: Mark Haddad

Email: mahaddad@cpp.edu, markhaddad03@gmail.com

Project you are applying for: Any project


---
## Quick Answer Questions
For the following questions answer as best you can, if you do not know, either make your best guess or skip the question. These questions are designed to cover all the potential roles for a project so it is not expected to know the answer to all of them. For the short answer ones answer is one or two sentences.

Sample:

Which of these is the number 5?
 - 1
 - 0
> - 5
 - 4

What is one difference between a float and an int?

> An int is a whole integer number while a float can be a decimal value.

### Questions:
---

**General**

What does an activity diagram show?
> Activity diagrams are a UML that rather than showing the flow and strcture between classes and objects, show a broader flow in the main activities occuring within a program or entire system. It shows aspects of sequential events of a system, or parts that branch and occur in parallel.

Which of these languages offers the lowest level of control and fastest execution?
 - Python
 - C#
 - Java
 > - C


What is the purpose of version control systems (VCS) such as Git or Mercurial?
> Version control systems are very helpful tools for managing and tracking changes in code over time, especially if done collaboratively with other people. Features like branching and version history make collaboration much smoother and more time efficient on the same source code.
---
**Embedded Systems**

Which level of cache would be accessible by only a single core on a multi-core chip?
 > - L1
 - L2
 - L3
 - All levels


Explain one difference between any of these 2 protocols: I2C, SPI, UART:
> I don't know. I am vaguely familiar with UART pinning for flight controllers on drones, which is useful for transmitting and receving signals needed for flight.

What is a feature Java has that C++ does not?
 - Object oriented classes
 - Lambda expressions
 - Data streams
 > - Implicit garbage collection


Name one major concern when developing for embedded systems and edge computing such as a deployed Jetson or Raspberry Pi:
> Some concerns are processing power, and incompatibility of software with the specific hardware. Work-arounds for processing power often involve in offloading heavy processes onto higher performance computers and then relaying information back to the microcontrollers. Software incompatibility often revolves around the operating system implemented on the microcontroller. Usually research should be done on external hardware and software used in an embedded system to make sure everything is compatible.

Which of the following is a job for the DHCP server?
 - Route packets out to the internet
 - Make particular ports available for access on the inter/intranet
 > - Assign IP addresses on the network
 - Look up what domain name maps to an address on the internet

---
**Linux**

What does the permission code 777 represent (as used in `chmod 777`)?
> chmod 777 grants read, write, and execute file permissions to all 3 levels: user, group, and others. Each 7 in 777 is the base 8 form of each permission correlating with each group. 7 in binary is 111, where each 1 indicates turning on each permission of rwx.

Which of these commands sets and environment variable in Linux? 
 > - export VAR=val
 - export $VAR=val 
 - echo VAR=val
 - echo $VAR=val


What is one major role of systemd?
> SystemD allows for process management on linux machines. You can use the `systemctl` command to check the status of, enable/disable, or activate/deactivate different processes.

---
**AI**

Which of these network architectures would be best suited for processing text?
 - Convolution Neural Network
 - Recurrent Neural Network
 - Multilayer Perceptron
 - U-Net


What is one solution to the vanishing gradient problem in backprop?


What is the traditional flow of interactions for a reinforcement learning agent?
 - Read the current state, take an action, environment updates state
 - Make a prediction, evaluate the loss from a target, update model with backprop
 - Generate result, compare result to similar objects of the class, improve discriminator and predictor


Briefly describe either branch and bound or dynamic programming:


What is the main challenge with implementing A*:
 - Picking the correct heuristic
 - Initialization parameters
 - Solution will not converge
 - Too long of an execution compared to other common pathfinders
