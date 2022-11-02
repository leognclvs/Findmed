import './pesquisa.css';
import Select from 'react-select';
import { useEffect, useState, useRef} from 'react';

function Pesquisa() {

  const [Options, setOptions] = useState([]);

  const selectRef = useRef(null);

  const onSubmmit = (event) => {
    event.preventDefault();
    console.log(selectRef.current.state.selectValue.map(a => a.value));
  }

  useEffect(() => {
    fetch("https://findmed.herokuapp.com/sintomas/")
      .then((res) => res.json())
      .then((res) => setOptions(res.map((sintoma) => ({value: sintoma.id_sint, label: sintoma.sintoma}))));
  }, []);

  return (
    <div className="pesquisa">
      <form onSubmit={onSubmmit}>
      <Select classNamePrefix="react-select"
            options={Options}
            isMulti
            placeholder="Digite os sintomas descritos:"
            ref={selectRef}
            />
      <button id='botao' type='submit' >Pesquisar</button>
      </form>
    </div>
  );
}

export default Pesquisa;