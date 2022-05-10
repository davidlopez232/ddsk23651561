# Generated by Django 4.0.4 on 2022-05-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('idactividades', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_actividad', models.CharField(max_length=45)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'actividades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('idarea', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_area', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('idasignatura', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_asignatura', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'asignatura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Barrios',
            fields=[
                ('idbarrios', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'barrios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cantitativa',
            fields=[
                ('idcantitativa', models.IntegerField(primary_key=True, serialize=False)),
                ('calificacion', models.CharField(max_length=45)),
                ('comentario', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'cantitativa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('idcargos', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cargo', models.CharField(max_length=45)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cargos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CentroCalificaciones',
            fields=[
                ('idcentro_calificaciones', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'centro_calificaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CertificadoEstudio',
            fields=[
                ('idcertificado_estudio', models.AutoField(primary_key=True, serialize=False)),
                ('grado', models.CharField(max_length=45)),
                ('repositorio', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'certificado_estudio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colegios',
            fields=[
                ('idcolegios', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_colegio', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'colegios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cualitativa',
            fields=[
                ('idcualitativa', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'cualitativa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idcurso', models.IntegerField(db_column='idCurso', primary_key=True, serialize=False)),
                ('nombre_curso', models.CharField(max_length=45)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('iddepartamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Documentos',
            fields=[
                ('iddocumentos', models.IntegerField(primary_key=True, serialize=False)),
                ('nombredocu', models.CharField(max_length=45)),
                ('respositorio', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'documentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoDocumento',
            fields=[
                ('idestado_codumento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'estado_documento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoMatricula',
            fields=[
                ('idestado_matricula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'estado_matricula',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('idgrado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_grado', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'grado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('idhorario', models.IntegerField(primary_key=True, serialize=False)),
                ('horario', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'horario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IngresarInfoMatricula',
            fields=[
                ('idingresar_info_matricula', models.IntegerField(primary_key=True, serialize=False)),
                ('ingresar_info_matriculacol', models.CharField(max_length=45)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ingresar_info_matricula',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Logros',
            fields=[
                ('idlogros', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_logro', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'logros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('idmatricula', models.IntegerField(db_column='idMatricula', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'matricula',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('idmunicipio', models.AutoField(db_column='idMunicipio', primary_key=True, serialize=False)),
                ('nombre_municipio', models.CharField(max_length=45)),
                ('ciudad_idciudad', models.IntegerField()),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificacionM',
            fields=[
                ('idnotificacion_m', models.IntegerField(primary_key=True, serialize=False)),
                ('mail_de', models.CharField(max_length=45)),
                ('mail_para', models.CharField(max_length=45)),
                ('info_no_valida', models.CharField(max_length=45)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'notificacion_m',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PeriodoAcademico',
            fields=[
                ('idperiodo_academico', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('fechainicio', models.DateField()),
                ('fechafin', models.DateField()),
            ],
            options={
                'db_table': 'periodo_academico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idpersona', models.IntegerField(primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=45)),
                ('segundo_nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('primer_apellido', models.CharField(max_length=45)),
                ('segundo_apellido', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=45)),
                ('identificacion', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('genero', models.CharField(db_column='Genero', max_length=45)),
                ('edad', models.CharField(max_length=45)),
                ('estado_civil', models.CharField(max_length=45)),
                ('nacionalidad', models.CharField(max_length=45)),
                ('fecha_expedicion_id', models.CharField(max_length=45)),
                ('lugar_expedicion_id', models.CharField(max_length=45)),
                ('documento_de_discapacidades_fisicas', models.CharField(blank=True, max_length=45, null=True)),
                ('copia_de_visa', models.CharField(blank=True, max_length=45, null=True)),
                ('recibo_de_pago_de_matricula', models.CharField(blank=True, db_column='recibo_de_pago_de_ matricula', max_length=45, null=True)),
                ('paz_y_salvo', models.CharField(blank=True, max_length=45, null=True)),
                ('observador', models.CharField(blank=True, db_column='Observador', max_length=45, null=True)),
                ('fotocopia_de_hdv', models.CharField(blank=True, max_length=45, null=True)),
                ('certificado_de_salud', models.CharField(blank=True, max_length=45, null=True)),
                ('certificado_de_la_eps', models.CharField(blank=True, max_length=45, null=True)),
                ('docuemto_de_retiro', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profesion',
            fields=[
                ('idprofesion', models.AutoField(primary_key=True, serialize=False)),
                ('profesion', models.CharField(max_length=45)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'profesion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RangoCalificacion',
            fields=[
                ('idrango_calificacion', models.IntegerField(db_column='idRango calificacion', primary_key=True, serialize=False)),
                ('rangoinicial', models.CharField(max_length=45)),
                ('rangofinal', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'rango calificacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCertificados',
            fields=[
                ('idcertificados', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipo_certificados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('idtipo_documento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_documento', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipo_documento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoNotificacion',
            fields=[
                ('idtipo_notificacion', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipo_notificacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPersona',
            fields=[
                ('idtipo_persona', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tipo_persona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Veredas',
            fields=[
                ('idveredas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_vereda', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'veredas',
                'managed': False,
            },
        ),
    ]
