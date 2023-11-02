/* home of app controller */
class AppController {
    getHomepage(request, response) {
      response.send('Hello Holberton School!');
    }
  }
  
  export default AppController;
  