import axios from 'axios';
import React, { Component } from 'react';
import PizzaUpdate from './pizzeriaupdate'

class PizzeriaDetail extends Component{

  constructor(props){
    super(props);
    this.state = {
      showComponent: false,
    };

  }
  updatePizzeriaDetails = (event)=>{
    this.setState({ showComponent: true, }); 
  }

  deletePizzeria = (event, obj)=>{
    axios.delete(process.env.REACT_APP_URL.concat(obj))
    .then(function (response){
      console.log(response);
    })
    .catch(function (error){
      console.log(error);
    });
  }

  render(){
    const obj = this.props.pizzeriaDetail;
    var detailStyle = {
      color:"yellow",
      border: "1px Solid yellow"
    }
    return( 
      <div style={detailStyle}>
        <h4>{obj.pizzeria_name}</h4>
        <h5>  
          Address: {obj.street} {obj.city} {obj.state} {obj.zip_code}
        </h5>
        <h6>Phone: {obj.phone_number} </h6>
        <p>{obj.description} </p>
        <button style={{backgroundColor:"white"}} onClick={this.updatePizzeriaDetails}>
          Update
        </button> 
        <button style={{backgroundColor:"white"}} onClick={this.deletePizzeria(obj.delete)}>
          Delete
        </button>
        {this.state.showComponent  ? <PizzaUpdate pizzeriaUpdate={obj}/> : null}
      </div>
    );
  }
}

export default PizzeriaDetail
