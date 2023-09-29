# Process Management Bash Scripts

This repository contains a collection of Bash scripts for managing processes and working with signals. These scripts provide examples of how to find process IDs (PIDs), list running processes, control process execution, and handle signals in the Bash shell.

## Scripts Overview

1. **0-what-is-my-pid**
   - Description: Prints the PID of the current Bash shell.

2. **1-list_your_processes**
   - Description: Lists information about all processes running on the system, including user, PID, CPU usage, memory usage, and more.

3. **2-show_your_bash_pid**
   - Description: Lists the PIDs of all running Bash processes.

4. **3-show_your_bash_pid_made_easy**
   - Description: Simplifies the task of listing the PIDs of running Bash processes using `pgrep`.

5. **4-to_infinity_and_beyond**
   - Description: Runs an infinite loop printing "To infinity and beyond" every 2 seconds. It serves as a simple example of a long-running process.

6. **5-dont_stop_me_now**
   - Description: Pauses the process created by `4-to_infinity_and_beyond` by sending a `SIGSTOP` signal.

7. **6-stop_me_if_you_can**
   - Description: Requests the process created by `4-to_infinity_and_beyond` to terminate gracefully by sending a `SIGTERM` signal.

8. **7-highlander**
   - Description: Runs an infinite loop similar to `4-to_infinity_and_beyond`, but traps the `SIGTERM` signal and prints "I am invincible!!!" when the signal is received, allowing it to continue running.

9. **8-beheaded_process**
   - Description: Forcefully terminates the process created by `7-highlander` by sending a `SIGKILL` signal (`kill -9`).

## Author

- Author: Noah Owens
- Email: noahowensdng@gmail.com

Feel free to explore and use these scripts for educational purposes or as templates for your own process management tasks.

