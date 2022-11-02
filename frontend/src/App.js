import './App.css';
import Cabecalho from './components/Cabecalho';
import Quadrado from './components/Quadrado';
import Pesquisa from './components/Pesquisa';
import Rodape from './components/Rodape';

function App() {
  return (
    <div className="App">
      <header>
        <Cabecalho />
      </header>
      <main>
        <Pesquisa />
        <Quadrado />
      </main>
      <footer>
        <Rodape />
      </footer>
    </div>
  );
}

export default App;
