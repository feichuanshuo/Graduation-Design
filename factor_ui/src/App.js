import React, {Component} from 'react';
//import {Redirect, Route, Switch} from "react-router-dom";
import {Button, Layout} from 'antd';
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
} from '@ant-design/icons';
import LeftMenu from "./components/left_menu";
import Header from "./components/header";
import './App.less';

const { Footer, Sider, Content } = Layout;


class App extends Component {
    state = {
        collapsed: true,
    }

    toggle = () => {
        this.setState({
            collapsed: !this.state.collapsed,
        });
    };

    render() {
        const {collapsed} = this.state
        return (
            <div className="app">
                <Layout>
                    <Header/>
                    <Layout>
                        <Sider className="sider" trigger={null} collapsible collapsed={this.state.collapsed}>
                            <LeftMenu/>
                            <Button
                                className="sider-button"
                                block
                                onClick={this.toggle}
                            >
                                <div className="sider-button-icon">
                                    {
                                        collapsed?<MenuUnfoldOutlined/>:<MenuFoldOutlined/>
                                    }
                                </div>
                            </Button>
                        </Sider>
                        <Layout>
                            <Content>Content</Content>
                            <Footer>Footer</Footer>
                        </Layout>
                    </Layout>
                </Layout>
            </div>
        );
    }
}

export default App;
