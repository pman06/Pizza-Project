import './App.css';
import PizzaList from './pizzerias/pizzeriaslist.js'


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src="https://image.similarpng.com/very-thumbnail/2020/06/Round-tasty-pizza-transparent-PNG.png" className="App-logo" alt="logo" />
        <p>
          Web app for Pizza Lovers
        </p>
        <h1
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Pizza Project
        </h1>
        <PizzaList/>
      </header>
    </div>
  );
}

export default App;
