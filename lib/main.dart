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
    return Scaffold(
      backgroundColor: Colors.blueGrey[100],
      appBar: AppBar(
        backgroundColor: Colors.blueGrey[400],
        title: const Text('Bufon Ninga Card App'),
        centerTitle: true,
        elevation: 0,
      ),
      body: const Padding(

        padding: EdgeInsets.all(50),
        
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Center(
              child:CircleAvatar(
                backgroundImage: AssetImage('assets/bufon.jpg'),
                radius: 40,
              )
            ),
            Divider(
              height: 60,
              color: Colors.grey,
            ),
            Text(
              'Name',
              style: TextStyle(
                color: Colors.blueGrey,
                letterSpacing: 2,
              ),
            ),
            SizedBox(height: 10),
            Text(
              'Bufon',
              style: TextStyle(
                color: Colors.cyan,
                letterSpacing: 2,
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(height: 20),
            Text(
              'Current Ninja Level',
              style: TextStyle(
                color: Colors.blueGrey,
                letterSpacing: 2,
              ),
            ),
            SizedBox(height: 10),
            Text(
              '8',
              style: TextStyle(
                color: Colors.cyan,
                letterSpacing: 2,
                fontSize: 28,
                fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(height: 20),
            Row(
              children: [
                Icon(Icons.email),
                SizedBox(width: 10),
                Text(
                  "bufon@bufon.com",
                  style: TextStyle(
                    color: Colors.cyan,
                    letterSpacing: 2
                  ),
                  ),
                
              ],
            ),
            
          ],

          
        ),
      ),
    );
  }
}
