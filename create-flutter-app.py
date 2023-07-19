import os

org = "com.example"
name = "app_name"
cmd = "flutter create --org " + org + " --project-name " + name + " .";
packages = [
 "cached_network_image",
 "collection", 
 "copy_with_extension",
 "equatable", 
 "extra_alignments", 
 "flextras", 
 "gap", 
 "get_it", 
 "get_it_mixin",
 "json_annotation",
 "modal_bottom_sheet", 
 "reactives", 
 "simple_rich_text", 
 "sized_context"
];
for p in packages: 
	cmd += " && flutter pub add " + packages[packages.index(p)]

packages = [
 "build_runner",
 "copy_with_extension_gen",
 "json_serializable", 
];

for p in packages: 
	cmd += " && flutter pub add " + packages[packages.index(p)]

# Create project
os.system(cmd);

# Replace main file
main = """import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Center(child: FlutterLogo()),
    );
  }
}"""

mainPath = "lib/main.dart"; 
os.remove(mainPath);
f = open(mainPath, "a")
f.write(main)
f.close()