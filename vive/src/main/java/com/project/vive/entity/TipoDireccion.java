package com.project.vive.entity;

import java.util.List;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name = "cat_tipodireccion")
public class TipoDireccion {
	@Id
	@GeneratedValue
	@Column(name = "idtipodireccion")
	private Integer id;
	
	@Column(name = "nombre")
	private String nombre;
	
	@Column(name = "descripcion")
	private String descripcion;

	@OneToMany(mappedBy = "tipoDireccion")
	private List<Direccion> direccionesPorTipo;
	
	public TipoDireccion(){
		super();
	}
	
	public TipoDireccion(Integer id, String nombre, String descripcion) {
		super();
		this.id = id;
		this.nombre = nombre;
		this.descripcion = descripcion;
	}


	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public List<Direccion> getDireccionesPorTipo() {
		return direccionesPorTipo;
	}

	public void setDireccionesPorTipo(List<Direccion> direccionesPorTipo) {
		this.direccionesPorTipo = direccionesPorTipo;
	}
	
	
}
