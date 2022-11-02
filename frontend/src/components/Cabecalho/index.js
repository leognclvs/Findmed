import './header.css';

function Cabecalho() {
    return (
        <div className="cabecalho">
            <img id='logo' src='./image/logo.svg' alt='Logo da página'/>
            <img id='nome' src='./image/nome.svg' alt='Nome da página'/>
        </div>
    )
}

export default Cabecalho;