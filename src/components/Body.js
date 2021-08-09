import PropTypes from 'prop-types'
import Button from './Button'

const Body = ({ title }) => {
    const onClick = () => {
        console.log('Click')
    }

    return (
        <body>
            <h2>{title}</h2>
           <Button color='grey' text='Show' onClick={onClick} />
           <Button color='black' text='Modify' />

        </body>
    )
}

Body.propTypes = {
    title: PropTypes.string,
}

export default Body
