import React, { Component } from 'react';
import PizzeriaDetail from './pizzeriadetail';
import axios from 'axios';

class PizzaList extends Component{
  state = {
    pizzeriasData: [],
    pizzeria: [],
  }

  constructor(props){
    super(props);
    this.state = {
      pizzeriasData: [],
      pizzeria: " ",
      showComponent: false,
    };
    this.getPizzaDetail= this.getPizzaDetail.bind(this);
    this.showPizzeriaDetails= this.showPizzeriaDetails.bind(this);
  }
  getPizzaDetail(item){
    axios.get("http://127.0.0.1:8000".concat(item.absolute_url))
    .then((response) => { 
      this.setState({pizzeria: response.data})
    })
    .catch(function (error){
        console.log(error)
    });
  }

  showPizzeriaDetails(item){
    this.getPizzaDetail(item);
    this.setState({ showComponent: true })
  }

  componentDidMount(){
    axios.get("http://127.0.0.1:8000/api/")
    .then((response) =>{
      this.setState({pizzeriasData: response.data})
    })
    .catch(function(error){
      console.log(error);
    })
  }

  render(){
      return(
          <div>
            {this.state.pizzeriasData.map((item) =>{
              {/* this.showPizzeriaDetails(item)*/}
              return <h3 onClick={() => this.showPizzeriaDetails(item)} key={item.id}>{item.pizzeria_name}, {item.city}</h3>
            })}

            {this.state.showComponent ? (
              <PizzeriaDetail pizzeriaDetail={this.state.pizzeria}/>
            ): null}
          </div>
        );
  }
}
export default PizzaList;
