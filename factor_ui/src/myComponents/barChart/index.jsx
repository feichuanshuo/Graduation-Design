import React, {Component} from 'react';
import './index.less';

class BarChart extends Component {

    barTagRef = React.createRef();
    rangeBarRef = React.createRef();
    valueBarRef = React.createRef();

    onMouseOver = (e) => {
        this.barTagRef.current.style.visibility = 'visible';
    }

    onMouseLeave = ()=>{
        this.barTagRef.current.style.visibility = 'hidden';
    }

    onMouseMove = (e) => {
        this.barTagRef.current.style.left = e.clientX + 'px';
        this.barTagRef.current.style.top = (e.clientY-70) + 'px';
    }

    componentDidMount() {
        this.valueBarRef.current.style.backgroundColor = this.props.color || 'red';
        this.rangeBarRef.current.style.width = this.props.width+'px' || '100%';
        this.valueBarRef.current.style.height = this.props.height+'px' || '20px';
        this.rangeBarRef.current.style.height = (this.props.height+2)+'px' || '22px';
        setTimeout(()=>{
            this.valueBarRef.current.style.width = this.props.value/this.props.range*this.props.width+'px';
        },200)
    }

    render() {
        const {value,tag} = this.props

        return (
            <div className={"bar-chart-box"}>
                <h5>{tag}</h5>
                <div className={"range-bar"} ref={this.rangeBarRef}>
                    <div className={"bar-tag"} ref={this.barTagRef}>
                        <div className={"bar-tag-title"}>{tag}</div>
                        <ul className={"bar-tag-content"}>
                            <li>
                                <span className={"bar-tag-pattern"}></span>
                                <span>value:</span>
                                <span className={"bar-tag-value"}>{value}</span>
                            </li>
                        </ul>
                    </div>
                    <div
                        className={"value-bar"}
                        ref = {this.valueBarRef}
                        style={{background:'red'}}
                        onMouseOver={this.onMouseOver}
                        onMouseLeave={this.onMouseLeave}
                        onMouseMove={this.onMouseMove}
                    ></div>
                </div>
            </div>
        );
    }
}




export default BarChart;
