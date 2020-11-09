import React from "react";

const people = "Kenny Jung, Satwik Misra, Ken Zou";

const date = new Date();
var year = date.getFullYear();

var hours = date.getHours();
var minutes = date.getMinutes();
var seconds = date.getSeconds();

function Footer() {
    return (
        <div>
            <p>Created by {people}. Copyright 2020-{year}.</p>
            <p>Page loaded at {hours + ":" + minutes + ":" + seconds}</p>
        </div>
    );
}

export default Footer;
