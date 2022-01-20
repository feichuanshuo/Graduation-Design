import React, {Component} from 'react';
import {Route, Routes} from "react-router-dom";
import {Button, Layout} from 'antd';
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
} from '@ant-design/icons';
import LeftMenu from "./components/left_menu";
import Header from "./components/header";
import SupplyData from "./components/content/supply_data";
import TransactionData from "./components/content/transaction_data";
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
            <Layout className="app">
                <Sider trigger={null} collapsible collapsed={this.state.collapsed}/>
                <Sider className="app-sider" trigger={null} collapsible collapsed={this.state.collapsed}>
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
                <Layout className="app-layout">
                    <header className="app-layout-header"/>
                    <Header/>
                    <Content>
                        <Routes>
                            <Route path={"/land_information/supply_data"} element={<SupplyData/>}/>
                            <Route path={"/land_information/transaction_data"} element={<TransactionData/>}/>
                        </Routes>
                    </Content>
                    <Footer>Footer</Footer>
                </Layout>
            </Layout>
        );
    }
}

export default App;
