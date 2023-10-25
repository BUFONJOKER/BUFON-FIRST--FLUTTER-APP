import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(
    home: Home(),
  ));
}

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blueGrey[600],
        title:  const Center(
          child:  Text('Bufon First App')
        ),
      ),
      body:Row(
        children: [
          Expanded(
            child: Container(
              color: Colors.red,
              padding: const EdgeInsets.all(20.0),
              child: const Text('1'),
              
            ),
          ),
          Expanded(
            child: Container(
              color: Colors.blue,
              padding: const EdgeInsets.all(20.0),
              child: const Text('2'),
            ),
          ),
          Expanded(
            child: Container(
              color: Colors.green,
              padding: const EdgeInsets.all(20.0),
              child: const Text('3'),
            ),
          ),
        ],
      )
    );
  }
}
