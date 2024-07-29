# ToobKito

ToobKito is a YouTube playlist downloader that allows you to download your favorite YouTube playlists with ease. This guide will help you set up and run ToobKito using Docker.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/toobkito.git
cd toobkito
```

### 2. Build the Docker Image

```bash
docker-compose build
```

### 3. Run ToobKito

```bash
docker-compose up || docker-compose run toobkito
```

### 4. Provide the Playlist URL

```bash
Enter the YouTube playlist URL: <link_of_play_list>
```

### 5. Provide the Folder Name

```bash
Enter the folder name: <folder_name>
```

### 6. Which videos to download?

```bash
Enter the range of videos to download (e.g. 1-5 or leave_blank_to_download_all): <start>-<end>
```

