import React,  {useState, useEffect} from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import axios from "axios";
import './styles.css';

const MorseToText = (props) => {
    const [text, setText] = useState(" ");
    return (
        <div>
            <header>
                <h1>CodMorse</h1>
                <p>Converta seu código morse em texto</p>
            </header>
            <Formik
                enableReinitialize 
                initialValues={{cod_morse:""}}
                validate={values => {
                    const errors = {};
                    if (!values.cod_morse) {
                        errors.nome = 'Código Morse é obrigatório!';
                    }
                    return errors;
                }}
                onSubmit={ async (values, {resetForm}) => {                
                                       
                    let param = {
                        codMorseParam: values.cod_morse
                    };
                    
                    const api = axios.create({
                        baseURL: "http://localhost",
                        responseType: "json"
                      });
                      
                    await api.get('/api/morse', {params: param})
                    .then(function (response) {  
                        if(response.data.data){
                            setText(text+response.data.data);                                                 
                        }
                        else{
                            toast.warn("Digite um código morse válido.");
                        }
                    }).catch(
                        function (response) {
                            toast.error("Problema interno. Tente novamente!");
                        }
                    );              
                }}
                >
                {({ isSubmitting }) => (
                    <Form className="form-padrao">
                        <label htmlFor="cod_morse">Código Morse:</label>
                        <Field type="text" name="cod_morse" placeholder=". -" required maxLength='5'/>
                        <ErrorMessage name="cod_morse" component="div" className="error-message"/>
     
                        <div className="submit-box">                            
                            <div>
                                <button type="submit">
                                    Converter
                                </button> 
                            </div>                         
                        </div>
                    </Form>
                )}
                </Formik>
                <ToastContainer position="bottom-right" />                
                <div className="box-text">
                    <h4>Resultado em texto:</h4>
                    <h2>{text}</h2>
                </div>
        </div>
    );
}

export default MorseToText;