import os


class CreateFlutterApp:
    """
    Creates a flutter project and configures it to clean architecture: MVC.

    It sets up the project with a separation of concerns,
    Facilitating maintainability and testability.

    Allowing you to focus on developing the business logic,
    Without worrying about the project's architecture.  
    """

    def __init__(self, arguments):
        """Initialize arguments, by those from terminal."""
        self.org = "com." + arguments.name
        self.name = arguments.name
        self.cmd = f"mkdir {self.name.capitalize()} && cd {self.name.capitalize()} &&"
        self.create_project()
        self.packages = ["cached_network_image"]
        self.add_packages()
        self.execute()
        self.replace_main_file()

    def create_project(self):
        self.cmd += "flutter create --org " + self.org + " --project-name " + \
            self.name + " ."

    def add_packages(self):
        if len(self.packages) != 0:
            for p in self.packages:
                if len(p) > 0:
                    self.cmd += "&& flutter pub add " + p

    def execute(self):
        os.system(self.cmd)

    def replace_main_file(self):
        main = """
    import 'package:flutter/material.dart';

    void main() => runApp(const MyApp());

    class MyApp extends StatelessWidget {
      const MyApp({Key? key}) : super(key: key);

      @override
      Widget build(BuildContext context) {
        return const MaterialApp(
          home: Center(child: FlutterLogo()),
        );
      }
    }
    """
        mainPath = f"{self.name.capitalize()}/lib/main.dart"
        os.remove(mainPath)
        f = open(mainPath, "a")
        f.write(main)
        f.close()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', dest='name', type=str,
                        help='Project name')
    args = parser.parse_args()
    CreateFlutterApp(args)
