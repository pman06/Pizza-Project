import React from 'react';
import axios from 'axios';

class PizzaUpdate extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            obj_to_update : this.props.pizzeriaUpdate,
            value : this.props.pizzeriaUpdate.description,
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event){
        this.setState({value: event.target.value});
    }

    handleSubmit(event){
        // event.preventDefault();
        axios.patch(process.env.REACT_APP_URL.concat(this.state.obj_to_update.update),
        {
            description : this.state.value,
        })
        .then((response)=>{
            console.log(response);
        })
        .catch(function (error){
            console.log(error);
        });
    }
    
    render(){
        const { value } = this.state;
        return(
            <div style={{color: 'Red', border:'1px solid red'}}>
                <form onSubmit={this.handleSubmit}>
                    <div>
                        <h6>Updating</h6>
                        <textarea value={value} onChange={this.handleChange}></textarea>
                    </div>
                    <input style={{ backgroundColor: 'white'}} type='submit' value='Submit'></input>
                </form>
            </div>
        );
    }
}

export default PizzaUpdate