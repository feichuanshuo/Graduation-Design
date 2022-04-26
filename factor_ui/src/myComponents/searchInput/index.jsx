import React, {Component} from 'react';
import {SearchOutlined} from '@ant-design/icons';
import './index.less';

class SearchInput extends Component {

    state = {
        searchHint:[]
    }

    inputRef = React.createRef();
    btnRef = React.createRef();
    ulRef = React.createRef();

    /*操作样式函数*/
    btnMouseDown = (e) => {
       this.btnRef.current.style.backgroundColor = '#096dd9';
    }

    btnMouseUp = (e) => {
        this.btnRef.current.style.backgroundColor = '#40a9ff';
        this.btnRef.current.style.outline = '#e3f1ff 3px solid';
    }

    btnMouseLeave = (e) => {
        this.btnRef.current.style.backgroundColor = '#178dfb';
        this.btnRef.current.style.outline = 'none';
    }

    inputBlur = (e) => {
        this.ulRef.current.style.display = 'none';
    }

    /*操作属性函数*/
    // 输入框内容改变时
    inputChange = (e) => {
        const {onChange} = this.props;
        const {searchHint} = this.state;
        setTimeout(()=>{
                if(searchHint.length!==0){
                    this.ulRef.current.style.display = 'block';
                }
                else{
                    this.ulRef.current.style.display = 'none';
                }
                onChange(e);
            },0
        )

    }

    /*暴露函数*/
    // 设置搜索提示
    setSearchHint = (searchHint)=>{
        this.setState({
            searchHint
        })
    }

    render() {
        const {searchHint} = this.state
        return (
            <div
                className={"detail-search"}
            >
                <input
                    ref={this.inputRef}
                    onBlur={this.inputBlur}
                    onChange={this.inputChange}
                />
                <button
                    ref={this.btnRef}
                    onMouseDown={this.btnMouseDown}
                    onMouseUp={this.btnMouseUp}
                    onMouseLeave={this.btnMouseLeave}
                >
                    搜索
                </button>
                <ul ref={this.ulRef}>
                    {
                        searchHint.map((item,index) => {
                            return (
                                <li key={index}><SearchOutlined /> {item}</li>
                            )
                        })
                    }
                </ul>
            </div>
        );
    }
}

export default SearchInput;
