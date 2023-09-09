import React from "react";
import Axios from "axios";

class Homepage extends React.Component {
  constructor() {
    super();
    this.state = {
      users: [], // Corrected the state property name
    };
  }

  componentDidMount() {
    const url = 'https://jsonplaceholder.typicode.com/users';
    Axios.get(url)
      .then((response) => {
        this.setState({ users: response.data }); // Update the state with fetched data
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }

  render() {
    console.log("---------------Ini akan dipasang");
    return (
      <div>
        {/* Render your user data here */}
        {this.state.users.map((user) => (
          <div key={user.id}>{user.name}</div>
        ))}
      </div>
    );
  }
}

export default Homepage;
