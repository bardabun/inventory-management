import { useState, useEffect } from 'react'
import Header from './components/Header'
import Body from './components/Body'
import Tasks from './components/Tasks'
import axios from 'axios'

function App() {
  const [tasks, setTasks] = useState([
    // {
    //   id: 1,
    //   supplier: 'Bruse',
    //   product: 'beans',
    //   arrivale: 'Aug 10th at 1:30pm',
    // },
    // {
    //   id: 2,  
    //   supplier: 'Tommy',
    //   product: 'Strawberries',
    //   arrivale: 'Aug 19th at 7:30am',
    // },
    // {
    //   id: 3,
    //   supplier: 'Louise',
    //   product: 'popcorn',
    //   arrivale: 'Sep 23th at 11:00am',
    // },
])

  // FECTH INTIAL DATA  
  const fetchInitial = async () => {
    // const { data, status } = await axios.get()
    // console.log(data);
    // if (status === 200) {
    //   setTasks(data);
    // }
  }

  useEffect(() => {
    fetchInitial();
  }, [])
  // GET REQUEST
  // const getData = () => {
  //   axios({
  //     nethod: 'get'
  //   })
  // }

  // Delete Task
  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id))
  }

  return (
    <div className="container">
    <Header title = 'let us help you manage your business'/>
    {tasks.length > 0 ? 
    (<Tasks tasks={tasks} onDelete={deleteTask} />) : (
      'No Tasks To Show'
    )}
    <Body title = 'This is the body'/>
    </div>
  );
}

export default App;
