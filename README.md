# TaskTracker

TaskTracker is a command-line application for managing tasks. It allows users to add, update, delete, and list tasks, providing a simple way to keep track of your to-do items.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- List all tasks
- Mark tasks as in-progress or done
- Filter tasks by status (to-do, in-progress, done)

## Requirements

- Python 3.x
- JSON file for storing tasks (`tasks.json`)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd TaskTracker
   ```

## Usage

Run the application from the command line with the following commands:

- To add a task:
  ```
  python main.py add "Task description"
  ```

- To update a task:
  ```
  python main.py update <task_id> "New task description"
  ```

- To delete a task:
  ```
  python main.py delete <task_id>
  ```

- To list all tasks:
  ```
  python main.py list
  ```

- To mark a task as in-progress:
  ```
  python main.py mark-in-progress <task_id>
  ```

- To mark a task as done:
  ```
  python main.py mark-done <task_id>
  ```

- To list all to-do tasks:
  ```
  python main.py list todo
  ```

- To list all completed tasks:
  ```
  python main.py list done
  ```

- To list all in-progress tasks:
  ```
  python main.py list in-progress
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.