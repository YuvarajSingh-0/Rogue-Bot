# Rogue Bot

Rogue Bot is a Discord bot that provides various features and functionalities to enhance your Discord server experience. It is built using the discord.py library and utilizes the concept of cogs for modular and organized code structure.


## Status
- Current State: :green_circle: **Online**


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

Rogue Bot is designed to make your Discord server more engaging and interactive. It offers a wide range of features, including moderation commands, utility commands, fun commands, and more. With the modular structure of cogs, it is easy to enable or disable specific features based on your server's needs.

## Features

- Moderation commands for managing your server effectively
- Utility commands for retrieving information or performing useful tasks
- Fun commands to entertain users with games and interactive features
- Customizable settings and configurations
- Easy-to-use command prefix and help system

## Tech Stack

Rogue Bot is built using the following technologies:

- [discord.py](https://discordpy.readthedocs.io/) - Python library for creating Discord bots
- [Python](https://www.python.org/) - Programming language used for bot development
- [GitHub](https://github.com/) - Version control and collaboration platform
- [Replit](https://replit.com/) - Online coding platform for hosting and running the bot

##Installation
------------

To install and set up Rogue Bot, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yuvarajsingh-0/Rogue-Bot.git
   ```

2. Navigate to the project directory:
   ```
   cd Rogue-Bot
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Discord bot token:
   - Create a new bot on the [Discord Developer Portal](https://discord.com/developers/applications).
   - Copy the bot token.
   - Create a `.env` file in the project directory.
   - Add the following line to the `.env` file, replacing `<your-bot-token>` with your actual bot token:
     
     ```
     TOKEN=<your-token>
     ```

5. Run the bot:
   ```
   python bot.py
   ```
## Usage

Rogue Bot uses the prefix `?` by default. You can change the prefix by modifying the `bot.py` file and adjusting the `command_prefix` parameter in the `Bot` initialization.

Some example commands:

- `?load <cog_name>`: Loads a specific cog.
- `?reload <cog_name>`: Reloads a specific cog.
- `?reloadAll`: Reloads all cogs.
- `?unload <cog_name>`: Unloads a specific cog.
- `?prefix`: Retrieves the current bot prefix.
- `?hello [message]`: Sends a hello message (optional).

Feel free to explore the available cogs and commands to further customize the bot's functionalities.

## Deployment

Rogue Bot can be easily deployed on Replit:

1. Create a new Replit project.
2. Copy the contents of your local Rogue Bot repository to the Replit project.
3. Configure the `.env` file in Replit and set your bot token.
4. Start the Replit project, and the bot will be up and running in your Discord server.

## Contributing

Contributions to Rogue Bot are highly appreciated! Whether you want to add new features, fix bugs, or improve the existing code, your contributions make a difference. To contribute to Rogue Bot, please follow the guidelines below:

### Getting Started

1. Fork the repository by clicking on the "Fork" button

 at the top right corner of this page. This will create a copy of the repository in your GitHub account.

2. Clone your forked repository to your local machine. Open your terminal and run the following command, replacing `<your-username>` with your GitHub username:

   ```bash
   https://github.com/YuvarajSingh-0/Rogue-Bot.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Rogue-Bot
   ```

4. Create a new branch to work on your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

### Making Changes

1. Open the project in your preferred text editor or IDE.

2. Make the necessary modifications and improvements to the codebase.

3. Test your changes locally to ensure they work as expected.

### Committing and Pushing

1. Once you are satisfied with your changes, commit them with a descriptive commit message:

   ```bash
   git commit -m "Add your commit message here"
   ```

2. Push your changes to your forked repository:

   ```bash
   git push origin feature/your-feature-name
   ```

### Creating a Pull Request

1. Visit your forked repository on GitHub.

2. Click on the "Pull Request" button to create a new pull request.

3. Provide a clear title and description for your pull request, explaining the changes you made.

4. Submit the pull request, and it will be reviewed by the project maintainers.

### Code Style and Guidelines

- Follow the existing code style and formatting conventions used in the project.

- Ensure your code is well-documented, providing clear comments where necessary.

## Accessing the Bot

To access Rogue Bot on Discord, [click here](https://discordapp.com/users/822173614236237865). This will redirect you to the Discord authorization page, where you can add the bot to your server. Make sure you have the necessary permissions to add a bot to your server.

## Thank You

Thank you for considering contributing to Rogue Bot! Your time and efforts are greatly appreciated. Together, let's make Rogue Bot even better!

If you have any questions or need assistance, feel free to reach out to me on discord at [UV](https://discordapp.com/users/702217200110665749). Happy contributing!
