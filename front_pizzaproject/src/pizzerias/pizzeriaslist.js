import React from 'react';
import PizzeriaDetail from './pizzeriadetail';
import PizzaForm from './pizzeriaform';
import axios from 'axios';


class PizzaList extends React.Component{
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
    axios.get(process.env.REACT_APP_URL.concat(item.absolute_url))
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
    axios.get(process.env.REACT_APP_URL.concat('/api/'))
    .then((response) =>{
      this.setState({pizzeriasData: response.data})
    })
    .catch(function(error){
      console.log(error);
    })
  }

  render(){
      var pizzaStyle = {
        cursor : "pointer",
      };
      return(
          <div>
          <PizzaForm/>
            {this.state.pizzeriasData.map((item) =>{
              return <h3  style = {pizzaStyle} onClick={() => this.showPizzeriaDetails(item)} key={item.id}>{item.pizzeria_name}, {item.city}</h3>
            })}

            {this.state.showComponent ? (
              <PizzeriaDetail pizzeriaDetail={this.state.pizzeria}/>
            ): null}
          </div>
        );
  }
}
export default PizzaList;
