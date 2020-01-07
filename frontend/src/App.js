import React, { Component } from 'react'
import DateTimePicker from 'react-datetime-picker';
import './App.css'
import { apiRoot } from './resources/config.js'

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {isLoading: false, recordLocator: '', firstName: '', lastName: '', date: new Date()};
    }

    handleRecordLocatorChange = (event) => {
        this.setState({recordLocator: event.target.value});
    };

    handleFirstNameChange = (event) => {
        this.setState({firstName: event.target.value});
    };

    handleLastNameChange = (event) => {
        this.setState({lastName: event.target.value});
    };

    handleDateChange = (date) => {
        this.setState({date: date});
    };

    postFlightCredentials = async () => {
        let {recordLocator, firstName, lastName, date} = this.state;
        let checkInDate = new Date(date);
        checkInDate.setHours(date.getHours() - 24);
        this.setState({isLoading: true});
        const response = await fetch(apiRoot + '/flight-credentials', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                recordLocator: recordLocator,
                firstName: firstName,
                lastName: lastName,
                dateTimeUTC: checkInDate.toUTCString()
            })
        }).then(response => response.json());
        alert(response.body || response['errorMessage']);
        this.setState({isLoading: false})
    };

    render() {
        let form =
            <form className={"App-header"} onSubmit={this.postFlightCredentials}>
                <label>Record Locator:<input type="text" value={this.state.recordLocator} onChange={this.handleRecordLocatorChange}/></label>
                <label>First Name:<input type="text" value={this.state.firstName} onChange={this.handleFirstNameChange}/></label>
                <label>Last Name:<input type="text" value={this.state.lastName} onChange={this.handleLastNameChange}/></label>
                <label>Local flight time:<DateTimePicker value={this.state.date} onChange={(date) => this.handleDateChange(date)}/></label>
              <input type="submit" value="Submit"/>
            </form>;

        return (
            <div className={"App-header"}>
                <h1>Southwest Checkin</h1>
                {this.state.isLoading || form}
                {this.state.isLoading && <h2>Loading...</h2>}
            </div>
        )
    }
}

export default App;