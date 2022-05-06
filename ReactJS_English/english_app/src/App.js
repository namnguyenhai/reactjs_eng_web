import MultiPlayer from './MultiPlayer.js'

import Postform from './components/Postform';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Postform/>
        <div className="App">
          <MultiPlayer
            urls={[
              'https://dictionary.cambridge.org/media/english/us_pron/g/goo/good_/good.mp3'
            ]}
          />
        </div>
      </header>
    </div>
  );
}

export default App;
