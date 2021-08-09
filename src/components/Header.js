import PropTypes from 'prop-types'
import Button from './Button'

const Header = ({ title }) => {
    const onClick = () => {
        console.log('CClick')
    }

    return (
        <header className='header'>
            <h1>{title}</h1>
           <Button color='grey' text='Show' onClick={onClick} />
           <Button color='black' text='Modify' />

        </header>
    )
}

Header.propTypes = {
    title: PropTypes.string,
}

export default Header
