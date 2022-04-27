import React, {Component} from 'react';
import {SearchOutlined,CloseOutlined} from '@ant-design/icons';
import './index.less';

class SearchInput extends Component {


    inputRef = React.createRef();
    iRef = React.createRef();
    btnRef = React.createRef();
    ulRef = React.createRef();

    /*操作样式函数*/
    // btn样式相关
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
    // 搜索框失去焦点则隐藏搜索提示
    inputBlur = (e) => {
        setTimeout(() => {
            this.ulRef.current.style.display = 'none';
        }, 200);
    }

    // 页面滚动则隐藏搜索提示
    handleScroll = ()=>{
        this.ulRef.current.style.display = 'none';
    }

    /*操作属性函数*/
    // 输入框内容改变时
    inputChange = (e) => {
        e.target.value == '' ? this.iRef.current.style.display='none': this.iRef.current.style.display='block';
        this.props.onChange(e);
        setTimeout(()=>{
            const {searchHint} = this.props;
            if(searchHint.length!==0){
                this.ulRef.current.style.display = 'block';
            }
            else{
                this.ulRef.current.style.display = 'none';
            }
        },100)
    }


    componentDidMount() {
        window.addEventListener("scroll", this.handleScroll);
    }

    componentWillUnmount() {
        window.removeEventListener("scroll", this.handleScroll);
    }

    render() {
        const {searchHint,onSearch} = this.props
        return (
            <div
                className={"detail-search"}
            >
                <input
                    ref={this.inputRef}
                    onBlur={this.inputBlur}
                    onChange={this.inputChange}
                />
                <i
                    ref={this.iRef}
                    onClick={()=>{
                        this.inputRef.current.value=''
                        this.iRef.current.style.display='none'
                    }}
                ><CloseOutlined/></i>
                <button
                    ref={this.btnRef}
                    onMouseDown={this.btnMouseDown}
                    onMouseUp={this.btnMouseUp}
                    onMouseLeave={this.btnMouseLeave}
                    onClick={()=>onSearch(this.inputRef.current.value)}
                >
                    搜索
                </button>
                <ul ref={this.ulRef}>
                    {
                        searchHint.map((item,index) => {
                            return (
                                <li
                                    key={index}
                                    onClick={()=>{
                                        onSearch(item)
                                        this.inputRef.current.value=item
                                }}><SearchOutlined /> {item}</li>
                            )
                        })
                    }
                </ul>
            </div>
        );
    }
}

export default SearchInput;
