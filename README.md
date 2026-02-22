<div align="center">
    <img src="https://github.com/Zhou-Shilin/picx-images-hosting/raw/master/image.1ovowaujq2.webp" alt="BukkitGPT Logo"/>
    <h1>BukkitGPT</h1>
    <p>AI-powered Minecraft Bukkit plugin generator</p>
    <a href="https://cynia.dev">Visit our website</a>  |  <a href="https://discord.gg/kTZtXw8s7r">Join our discord</a>
</div>


> ⚠️ **Project Status: Development Paused**
> 
> Thank you to everyone who has supported this project! As we continued to explore the intersection of AI and Minecraft, we discovered a much more elegant and native solution. Therefore, active development on this project has been paused. We highly recommend all users check out our brand-new, next-generation project: **[MineClawd](https://github.com/Zhou-Shilin/MineClawd)**.
> 
> Compared to this project (which requires out-of-game generation, tedious setups, server restarts, or external schematic imports), **MineClawd** brings the highly autonomous **OpenClaw** AI agent framework directly into Minecraft!
> 
> **Why switch to MineClawd?**
> * 🧠 **Ultimate Freedom**: Accomplish almost *anything* in-game by executing instant or persistent KubeJS code.
> * 📦 **Dynamic Pseudo-Creation**: Dynamically register new items, blocks, and fluids on the fly.
> * ⚡ **Seamless Experience**: Runs smoothly as a Server-only mod with immediate effects. An optional Client mod is also available for a user-friendly GUI.
> 
> Everything this old project tried to achieve, MineClawd does better, faster, and seamlessly in-game.
> 
> 🌟 **Discover and Support MineClawd:**
> * **Modrinth:** [Download here](https://modrinth.com/mod/mineclawd) (Supports NeoForge 1.21.1 | Forge 1.20.1 | Fabric 1.20.1)
> * **GitHub:** [Zhou-Shilin/MineClawd](https://github.com/Zhou-Shilin/MineClawd) (If you like the concept, please drop a ⭐ Star!)

## Introduction
> Give the LLM your idea, AI generates customized Minecraft server plugins with one click, which is suitable for Bukkit, Spigot, Paper, Purpur, Arclight, CatServer, Magma, Mohist and other Bukkit-based servers.

[Watch the Video Tutorial](https://youtu.be/ubqH-e4aaRU?si=p0uxiJbzXP9vYDuQ)

BukkitGPT is an open source, free, AI-powered Minecraft Bukkit plugin generator. It was developed for minecraft server owners who are not technically savvy but need to implement all kinds of customized small plugins. From code to build, debug, all done by the LLM.


## CyniaAI WebApp

> [!WARNING]
> There're big differences between *BukkitGPT-v3 WebUI* and *CyniaAI WebApp*. BukkitGPT is a self-hosted, free, open-source, community-driven project, while CyniaAI WebApp is a paid, cloud-hosted service that provides a more user-friendly experience for non-developers.
> Issues and questions about CyniaAI WebApp should be directed to our [Discord Server](https://discord.gg/kTZtXw8s7r).

Don't want to deal with Python, Maven, BuildTools, and other complicated environments?
Hey! Here's [the CyniaAI WebApp](https://cynia.dev) designed just for you - generate plugins **even on your phone**!

*The service is paid since the API key we are using is not free. You can get 1 key for 5 generations for $1 [here](https://afdian.com/item/b839835461e311efbd1252540025c377)

*The WebApp edition doesn't support plugin editing feature yet, but we are working on it.

## Features

- Automatically generate plugin code based on the user's description.
- Edit existing plugins.
- Brand new Streamlit UI.

### Other projects of CyniaAI Team
- [x] Bukkit plugin generator. {*.jar} ([BukkitGPT-v3](https://github.com/CyniaAI/BukkitGPT-v3))
- [x] Structure generator. {*.schem} ([BuilderGPT](https://github.com/CyniaAI/BuilderGPT))
- [ ] Serverpack generator. {*.zip} (ServerpackGPT or ServerGPT, or..?)
- [ ] Have ideas or want to join our team? Send [us](mailto:admin@baimoqilin.top) an email!

## Requirements
You can use BukkitGPT on any computer with [Java](https://www.azul.com/downloads/), [Maven](https://maven.apache.org/), [Python 3+](https://www.python.org/) **AND** [BuildTools](https://github.com/CyniaAI/BukkitGPT-v3#the-pom-for-orgspigotmcspigotjar1132-r01-snapshot-is-missing) installed. 

## Quick Start

1. Clone the repository and install the dependencies with command:
```bash
git clone https://github.com/CyniaAI/BukkitGPT-v3
cd BukkitGPT-v3
python -m venv venv
source venv/bin/activate # for Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```
2. Copy `.env.example` to `.env` and edit it to set `LLM_PROVIDER` (e.g. `openai`, `anthropic`, `google`) and fill in your provider API key.
3. Run bash command `streamlit web.py` to start the web application.
4. Open your browser and go to `http://localhost:8501` to access the web application.
5. Enjoy!

## Troubleshooting

### The POM for org.spigotmc:spigot:jar:1.13.2-R0.1-SNAPSHOT is missing
1. [Download BuildTools](https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar) and place it in *an empty folder*.
2. Open the file.
3. Choose `1.13.2` in `Settings/Select Version`.
4. Click `Compile` in the bottom right corner and let it finish.
5. Go to your BukkitGPT folder, execute `build.bat` in `projects/<artifact_name_of_your_plugin>`.
6. You'll find your plugin in `projects/<artifact_name_of_your_plugin>/target` folder.

### 'mvn' is not recognized as an internal or external command

** If you have not installed Maven, please follow the steps below: **
1. Make sure you have [Maven](https://maven.apache.org/) installed.
2. Add the Maven `bin` directory to your system `PATH` environment variable.
3. Restart your terminal or command prompt.

** If you are sure that you installed Maven and it does work everywhere else, but not in BukkitGPT-v3: **

Sometimes the terminal does not use the system `PATH` environment variable, so you need to set it manually. You can do this by adding the following line to your `.env` file:

```plaintext
PATH=/path/to/maven/bin:$PATH
```


## Contributing
If you like the project, you can give the project a star, or [submit an issue](https://github.com/CyniaAI/BukkitGPT-v3/issues) or [pull request](https://github.com/CyniaAI/BukkitGPT-v3/pulls) to help make it better.

## License
```
Copyright [2024] [CyniaAI Team]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
