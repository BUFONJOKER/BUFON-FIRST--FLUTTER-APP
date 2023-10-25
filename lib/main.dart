import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(
    home: Home(),
  ));
}

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {

  var bufonNinjaLevel = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[100],
      appBar: AppBar(
        backgroundColor: Colors.blueGrey[400],
        title: const Text('Bufon Ninga Card App'),
        centerTitle: true,
        elevation: 0,
      ),
      floatingActionButton: FloatingActionButton(
        backgroundColor: Colors.blueGrey[400],
        child: const Icon(Icons.add),
        onPressed: ()=> {
          setState(() {
            bufonNinjaLevel +=1;
          })
        }),
        
      body: Padding(
        padding: const EdgeInsets.all(50),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            const Center(
                child: CircleAvatar(
              backgroundImage: AssetImage('assets/bufon.jpg'),
              radius: 40,
            )),
            const Divider(
              height: 60,
              color: Colors.grey,
            ),
            const Text(
              'Name',
              style: TextStyle(
                color: Colors.blueGrey,
                letterSpacing: 2,
              ),
            ),
            const SizedBox(height: 10),
            const Text(
              'Bufon',
              style: TextStyle(
                color: Colors.cyan,
                letterSpacing: 2,
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),
            const Text(
              'Current Ninja Level',
              style: TextStyle(
                color: Colors.blueGrey,
                letterSpacing: 2,
              ),
            ),
            const SizedBox(height: 10),
            Text(
              '$bufonNinjaLevel',
              style: const TextStyle(
                color: Colors.cyan,
                letterSpacing: 2,
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 20),
            const Row(
              children: [
                Icon(Icons.email),
                SizedBox(width: 10),
                Text(
                  "bufon@bufon.com",
                  style: TextStyle(color: Colors.cyan, letterSpacing: 2),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

