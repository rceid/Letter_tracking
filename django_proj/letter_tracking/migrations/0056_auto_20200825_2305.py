# Generated by Django 3.1 on 2020-08-25 23:05

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('letter_tracking', '0055_auto_20200825_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='caucus',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('', 'N/a'), ('CHC', 'CHC'), ('Tri Caucus', 'Tri Caucus')], max_length=100),
        ),
        migrations.AlterField(
            model_name='letter',
            name='cosigners',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', 'N/a'), ('Alexander Lamar', 'Alexander Lamar'), ('Baldwin Tammy', 'Baldwin Tammy'), ('Barrasso John', 'Barrasso John'), ('Bennet Michael', 'Bennet Michael'), ('Blackburn Marsha', 'Blackburn Marsha'), ('Blumenthal Richard', 'Blumenthal Richard'), ('Blunt Roy', 'Blunt Roy'), ('Booker Cory', 'Booker Cory'), ('Boozman John', 'Boozman John'), ('Braun Mike', 'Braun Mike'), ('Brown Sherrod', 'Brown Sherrod'), ('Burr Richard', 'Burr Richard'), ('Cantwell Maria', 'Cantwell Maria'), ('Capito Shelley', 'Capito Shelley'), ('Cardin Benjamin', 'Cardin Benjamin'), ('Carper Thomas', 'Carper Thomas'), ('Casey Bob', 'Casey Bob'), ('Cassidy Bill', 'Cassidy Bill'), ('Collins Susan', 'Collins Susan'), ('Coons Chris', 'Coons Chris'), ('Cornyn John', 'Cornyn John'), ('Cortez Masto Catherine', 'Cortez Masto Catherine'), ('Cotton Tom', 'Cotton Tom'), ('Cramer Kevin', 'Cramer Kevin'), ('Crapo Michael', 'Crapo Michael'), ('Cruz Ted', 'Cruz Ted'), ('Daines Steve', 'Daines Steve'), ('Duckworth Tammy', 'Duckworth Tammy'), ('Durbin Richard', 'Durbin Richard'), ('Enzi Michael', 'Enzi Michael'), ('Ernst Joni', 'Ernst Joni'), ('Feinstein Dianne', 'Feinstein Dianne'), ('Fischer Deb', 'Fischer Deb'), ('Gardner Cory', 'Gardner Cory'), ('Gillibrand Kirsten', 'Gillibrand Kirsten'), ('Graham Lindsey', 'Graham Lindsey'), ('Grassley Charles', 'Grassley Charles'), ('Harris Kamala', 'Harris Kamala'), ('Hassan Maggie', 'Hassan Maggie'), ('Hawley Josh', 'Hawley Josh'), ('Heinrich Martin', 'Heinrich Martin'), ('Hirono Mazie', 'Hirono Mazie'), ('Hoeven John', 'Hoeven John'), ('Hyde-Smith Cindy', 'Hyde-Smith Cindy'), ('Inhofe James', 'Inhofe James'), ('Johnson Ron', 'Johnson Ron'), ('Jones Doug', 'Jones Doug'), ('Kaine Tim', 'Kaine Tim'), ('Kennedy John', 'Kennedy John'), ('King Angus', 'King Angus'), ('Klobuchar Amy', 'Klobuchar Amy'), ('Lankford James', 'Lankford James'), ('Leahy Patrick', 'Leahy Patrick'), ('Lee Mike', 'Lee Mike'), ('Loeffler Kelly', 'Loeffler Kelly'), ('Manchin Joe', 'Manchin Joe'), ('Markey Edward', 'Markey Edward'), ('McConnell Mitch', 'McConnell Mitch'), ('McSally Martha', 'McSally Martha'), ('Menendez Bob', 'Menendez Bob'), ('Merkley Jeff', 'Merkley Jeff'), ('Moran Jerry', 'Moran Jerry'), ('Murkowski Lisa', 'Murkowski Lisa'), ('Murphy Christopher', 'Murphy Christopher'), ('Murray Patty', 'Murray Patty'), ('Paul Rand', 'Paul Rand'), ('Perdue David', 'Perdue David'), ('Peters Gary', 'Peters Gary'), ('Portman Rob', 'Portman Rob'), ('Reed Jack', 'Reed Jack'), ('Risch Jim', 'Risch Jim'), ('Roberts Pat', 'Roberts Pat'), ('Romney Mitt', 'Romney Mitt'), ('Rosen Jacky', 'Rosen Jacky'), ('Rounds Mike', 'Rounds Mike'), ('Rubio Marco', 'Rubio Marco'), ('Sanders Bernie', 'Sanders Bernie'), ('Sasse Ben', 'Sasse Ben'), ('Schatz Brian', 'Schatz Brian'), ('Schumer Charles', 'Schumer Charles'), ('Scott Rick', 'Scott Rick'), ('Scott Tim', 'Scott Tim'), ('Shaheen Jeanne', 'Shaheen Jeanne'), ('Shelby Richard', 'Shelby Richard'), ('Sinema Kyrsten', 'Sinema Kyrsten'), ('Smith Tina', 'Smith Tina'), ('Stabenow Debbie', 'Stabenow Debbie'), ('Sullivan Dan', 'Sullivan Dan'), ('Tester Jon', 'Tester Jon'), ('Thune John', 'Thune John'), ('Tillis Thom', 'Tillis Thom'), ('Toomey Patrick', 'Toomey Patrick'), ('Udall Tom', 'Udall Tom'), ('Van Hollen Chris', 'Van Hollen Chris'), ('Warner Mark', 'Warner Mark'), ('Warren Elizabeth', 'Warren Elizabeth'), ('Whitehouse Sheldon', 'Whitehouse Sheldon'), ('Wicker Roger', 'Wicker Roger'), ('Wyden Ron', 'Wyden Ron'), ('Young Todd', 'Young Todd'), ('Abraham Ralph', 'Abraham Ralph'), ('Adams Alma', 'Adams Alma'), ('Aderholt Robert', 'Aderholt Robert'), ('Aguilar Pete', 'Aguilar Pete'), ('Allen Rick', 'Allen Rick'), ('Allred Colin', 'Allred Colin'), ('Amash Justin', 'Amash Justin'), ('Amodei Mark', 'Amodei Mark'), ('Armstrong Kelly', 'Armstrong Kelly'), ('Arrington Jodey', 'Arrington Jodey'), ('Axne Cindy', 'Axne Cindy'), ('Babin Brian', 'Babin Brian'), ('Bacon Don', 'Bacon Don'), ('Baird Jim', 'Baird Jim'), ('Balderson Troy', 'Balderson Troy'), ('Banks Jim', 'Banks Jim'), ('Barr Andy', 'Barr Andy'), ('Diaz Barragan Nanette', 'Diaz Barragan Nanette'), ('Bass Karen', 'Bass Karen'), ('Beatty Joyce', 'Beatty Joyce'), ('Bera Ami', 'Bera Ami'), ('Bergman Jack', 'Bergman Jack'), ('Beyer Don', 'Beyer Don'), ('Biggs Andy', 'Biggs Andy'), ('Bilirakis Gus', 'Bilirakis Gus'), ('Bishop Dan', 'Bishop Dan'), ('Bishop Rob', 'Bishop Rob'), ('Bishop Sanford', 'Bishop Sanford'), ('Blumenauer Earl', 'Blumenauer Earl'), ('Blunt Rochester Lisa', 'Blunt Rochester Lisa'), ('Bonamici Suzanne', 'Bonamici Suzanne'), ('Bost Mike', 'Bost Mike'), ('Boyle Brendan', 'Boyle Brendan'), ('Brady Kevin', 'Brady Kevin'), ('Brindisi Anthony', 'Brindisi Anthony'), ('Brooks Mo', 'Brooks Mo'), ('Brooks Susan', 'Brooks Susan'), ('Brown Anthony', 'Brown Anthony'), ('Brownley Julia', 'Brownley Julia'), ('Buchanan Vern', 'Buchanan Vern'), ('Buck Ken', 'Buck Ken'), ('Bucshon Larry', 'Bucshon Larry'), ('Budd Ted', 'Budd Ted'), ('Burchett Tim', 'Burchett Tim'), ('Burgess Mike', 'Burgess Mike'), ('Bustos Cheri', 'Bustos Cheri'), ('Butterfield G.K.', 'Butterfield G.K.'), ('Byrne Bradley', 'Byrne Bradley'), ('Calvert Ken', 'Calvert Ken'), ('Carbajal Salud', 'Carbajal Salud'), ('Cardenas Tony', 'Cardenas Tony'), ('Carson Andre', 'Carson Andre'), ('Carter Buddy', 'Carter Buddy'), ('Carter John', 'Carter John'), ('Cartwright Matt', 'Cartwright Matt'), ('Case Ed', 'Case Ed'), ('Casten Sean', 'Casten Sean'), ('Castor Kathy', 'Castor Kathy'), ('Castro Joaquin', 'Castro Joaquin'), ('Chabot Steve', 'Chabot Steve'), ('Cheney Liz', 'Cheney Liz'), ('Chu Judy', 'Chu Judy'), ('Cicilline David', 'Cicilline David'), ('Cisneros Gil', 'Cisneros Gil'), ('Clark Katherine', 'Clark Katherine'), ('Clarke Yvette', 'Clarke Yvette'), ('Clay Lacy', 'Clay Lacy'), ('Cleaver Emanuel', 'Cleaver Emanuel'), ('Cline Ben', 'Cline Ben'), ('Cloud Michael', 'Cloud Michael'), ('Clyburn Jim', 'Clyburn Jim'), ('Cohen Steve', 'Cohen Steve'), ('Cole Tom', 'Cole Tom'), ('Collins Doug', 'Collins Doug'), ('Comer James', 'Comer James'), ('Conaway Mike', 'Conaway Mike'), ('Connolly Gerry', 'Connolly Gerry'), ('Cook Paul', 'Cook Paul'), ('Cooper Jim', 'Cooper Jim'), ('Correa Lou', 'Correa Lou'), ('Costa Jim', 'Costa Jim'), ('Courtney Joe', 'Courtney Joe'), ('Cox TJ', 'Cox TJ'), ('Craig Angie', 'Craig Angie'), ('Crawford Rick', 'Crawford Rick'), ('Crenshaw Dan', 'Crenshaw Dan'), ('Crist Charlie', 'Crist Charlie'), ('Crow Jason', 'Crow Jason'), ('Cuellar Henry', 'Cuellar Henry'), ('Cunningham Joe', 'Cunningham Joe'), ('Curtis John', 'Curtis John'), ('Davids Sharice', 'Davids Sharice'), ('Davidson Warren', 'Davidson Warren'), ('Davis Danny', 'Davis Danny'), ('Davis Rodney', 'Davis Rodney'), ('Davis Susan', 'Davis Susan'), ('Dean Madeleine', 'Dean Madeleine'), ('DeFazio Peter', 'DeFazio Peter'), ('DeGette Diana', 'DeGette Diana'), ('DeLauro Rosa', 'DeLauro Rosa'), ('DelBene Suzan', 'DelBene Suzan'), ('Delgado Antonio', 'Delgado Antonio'), ('Demings Val', 'Demings Val'), ('DeSaulnier Mark', 'DeSaulnier Mark'), ('DesJarlais Scott', 'DesJarlais Scott'), ('Deutch Ted', 'Deutch Ted'), ('Diaz-Balart Mario', 'Diaz-Balart Mario'), ('Dingell Debbie', 'Dingell Debbie'), ('Doggett Lloyd', 'Doggett Lloyd'), ('Doyle Mike', 'Doyle Mike'), ('Duncan Jeff', 'Duncan Jeff'), ('Dunn Neal', 'Dunn Neal'), ('Emmer Tom', 'Emmer Tom'), ('Engel Eliot', 'Engel Eliot'), ('Escobar Veronica', 'Escobar Veronica'), ('Eshoo Anna', 'Eshoo Anna'), ('Espaillat Adriano', 'Espaillat Adriano'), ('Estes Ron', 'Estes Ron'), ('Evans Dwight', 'Evans Dwight'), ('Ferguson Drew', 'Ferguson Drew'), ('Finkenauer Abby', 'Finkenauer Abby'), ('Fitzpatrick Brian', 'Fitzpatrick Brian'), ('Fleischmann Chuck', 'Fleischmann Chuck'), ('Fletcher Lizzie', 'Fletcher Lizzie'), ('Flores Bill', 'Flores Bill'), ('Fortenberry Jeff', 'Fortenberry Jeff'), ('Foster Bill', 'Foster Bill'), ('Foxx Virginia', 'Foxx Virginia'), ('Frankel Lois', 'Frankel Lois'), ('Fudge Marcia', 'Fudge Marcia'), ('Fulcher Russ', 'Fulcher Russ'), ('Gabbard Tulsi', 'Gabbard Tulsi'), ('Gaetz Matt', 'Gaetz Matt'), ('Gallagher Mike', 'Gallagher Mike'), ('Gallego Ruben', 'Gallego Ruben'), ('Garamendi John', 'Garamendi John'), ('Garcia Chuy', 'Garcia Chuy'), ('Garcia Sylvia', 'Garcia Sylvia'), ('Gianforte Greg', 'Gianforte Greg'), ('Gibbs Bob', 'Gibbs Bob'), ('Gohmert Louie', 'Gohmert Louie'), ('Golden Jared', 'Golden Jared'), ('Gomez Jimmy', 'Gomez Jimmy'), ('Gonzalez Anthony', 'Gonzalez Anthony'), ('Gonzalez Vicente', 'Gonzalez Vicente'), ('Gonzalez-Colon Jenniffer', 'Gonzalez-Colon Jenniffer'), ('Gooden Lance', 'Gooden Lance'), ('Gosar Paul', 'Gosar Paul'), ('Gottheimer Josh', 'Gottheimer Josh'), ('Granger Kay', 'Granger Kay'), ('Graves Garret', 'Graves Garret'), ('Graves Tom', 'Graves Tom'), ('Graves Sam', 'Graves Sam'), ('Green Al', 'Green Al'), ('Green Mark', 'Green Mark'), ('Griffith Morgan', 'Griffith Morgan'), ('Grijalva Raul', 'Grijalva Raul'), ('Grothman Glenn', 'Grothman Glenn'), ('Guest Michael', 'Guest Michael'), ('Guthrie Brett', 'Guthrie Brett'), ('Haaland Deb', 'Haaland Deb'), ('Hagedorn Jim', 'Hagedorn Jim'), ('Harder Josh', 'Harder Josh'), ('Harris Andy', 'Harris Andy'), ('Hartzler Vicky', 'Hartzler Vicky'), ('Hastings Alcee', 'Hastings Alcee'), ('Hayes Jahana', 'Hayes Jahana'), ('Heck Denny', 'Heck Denny'), ('Hern Kevin', 'Hern Kevin'), ('Herrera Beutler Jaime', 'Herrera Beutler Jaime'), ('Hice Jody', 'Hice Jody'), ('Higgins Brian', 'Higgins Brian'), ('Higgins Clay', 'Higgins Clay'), ('Hill French', 'Hill French'), ('Himes Jim', 'Himes Jim'), ('Holding George', 'Holding George'), ('Hollingsworth Trey', 'Hollingsworth Trey'), ('Horn Kendra', 'Horn Kendra'), ('Horsford Steven', 'Horsford Steven'), ('Houlahan Chrissy', 'Houlahan Chrissy'), ('Hoyer Steny', 'Hoyer Steny'), ('Hudson Richard', 'Hudson Richard'), ('Huffman Jared', 'Huffman Jared'), ('Huizenga Bill', 'Huizenga Bill'), ('Hurd Will', 'Hurd Will'), ('Jacobs Christopher', 'Jacobs Christopher'), ('Jackson Lee Sheila', 'Jackson Lee Sheila'), ('Jayapal Pramila', 'Jayapal Pramila'), ('Jeffries Hakeem', 'Jeffries Hakeem'), ('Johnson Dusty', 'Johnson Dusty'), ('Johnson Eddie Bernice ', 'Johnson Eddie Bernice '), ('Johnson Hank', 'Johnson Hank'), ('Johnson Mike', 'Johnson Mike'), ('Johnson Bill', 'Johnson Bill'), ('Jordan Jim', 'Jordan Jim'), ('Joyce Dave', 'Joyce Dave'), ('Joyce John', 'Joyce John'), ('Kaptur Marcy', 'Kaptur Marcy'), ('Katko John', 'Katko John'), ('Keating Bill', 'Keating Bill'), ('Keller Fred', 'Keller Fred'), ('Kelly Mike', 'Kelly Mike'), ('Kelly Robin', 'Kelly Robin'), ('Kelly Trent', 'Kelly Trent'), ('Kennedy III Joe', 'Kennedy III Joe'), ('Khanna Ro', 'Khanna Ro'), ('Kildee Dan', 'Kildee Dan'), ('Kilmer Derek', 'Kilmer Derek'), ('Kim Andy', 'Kim Andy'), ('Kind Ron', 'Kind Ron'), ('King Pete', 'King Pete'), ('King Steve', 'King Steve'), ('Kinzinger Adam', 'Kinzinger Adam'), ('Kirkpatrick Ann', 'Kirkpatrick Ann'), ('Krishnamoorthi Raja', 'Krishnamoorthi Raja'), ('Kuster Ann', 'Kuster Ann'), ('Kustoff David', 'Kustoff David'), ('LaHood Darin', 'LaHood Darin'), ('LaMalfa Doug', 'LaMalfa Doug'), ('Lamb Conor', 'Lamb Conor'), ('Lamborn Doug', 'Lamborn Doug'), ('Langevin Jim', 'Langevin Jim'), ('Larsen Rick', 'Larsen Rick'), ('Larson John', 'Larson John'), ('Latta Bob', 'Latta Bob'), ('Lawrence Brenda', 'Lawrence Brenda'), ('Lawson Al', 'Lawson Al'), ('Lee Barbara', 'Lee Barbara'), ('Lee Susie', 'Lee Susie'), ('Lesko Debbie', 'Lesko Debbie'), ('Levin Andy', 'Levin Andy'), ('Levin Mike', 'Levin Mike'), ('Lewis John', 'Lewis John'), ('Lieu Ted', 'Lieu Ted'), ('Lipinski Dan', 'Lipinski Dan'), ('Loebsack Dave', 'Loebsack Dave'), ('Lofgren Zoe', 'Lofgren Zoe'), ('Long Billy', 'Long Billy'), ('Loudermilk Barry', 'Loudermilk Barry'), ('Lowenthal Alan', 'Lowenthal Alan'), ('Lowey Nita', 'Lowey Nita'), ('Lucas Frank', 'Lucas Frank'), ('Luetkemeyer Blaine', 'Luetkemeyer Blaine'), ('Ray Lujan Ben', 'Ray Lujan Ben'), ('Luria Elaine', 'Luria Elaine'), ('Lynch Stephen', 'Lynch Stephen'), ('Malinowski Tom', 'Malinowski Tom'), ('Maloney Carolyn', 'Maloney Carolyn'), ('Maloney Sean Patrick ', 'Maloney Sean Patrick '), ('Marchant Kenny', 'Marchant Kenny'), ('Marshall Roger', 'Marshall Roger'), ('Massie Thomas', 'Massie Thomas'), ('Mast Brian', 'Mast Brian'), ('Matsui Doris', 'Matsui Doris'), ('McAdams Ben', 'McAdams Ben'), ('McBath Lucy', 'McBath Lucy'), ('McCarthy Kevin', 'McCarthy Kevin'), ('McCaul Michael', 'McCaul Michael'), ('McClintock Tom', 'McClintock Tom'), ('McCollum Betty', 'McCollum Betty'), ('McEachin Donald', 'McEachin Donald'), ('McGovern Jim', 'McGovern Jim'), ('McHenry Patrick', 'McHenry Patrick'), ('McKinley David', 'McKinley David'), ('McMorris Rodgers Cathy', 'McMorris Rodgers Cathy'), ('McNerney Jerry', 'McNerney Jerry'), ('Meeks Gregory', 'Meeks Gregory'), ('Meng Grace', 'Meng Grace'), ('Meuser Dan', 'Meuser Dan'), ('Mfume Kweisi', 'Mfume Kweisi'), ('Miller Carol', 'Miller Carol'), ('Mitchell Paul', 'Mitchell Paul'), ('Moolenaar John', 'Moolenaar John'), ('Mooney Alex', 'Mooney Alex'), ('Moore Gwen', 'Moore Gwen'), ('Morelle Joe', 'Morelle Joe'), ('Moulton Seth', 'Moulton Seth'), ('Mucarsel-Powell Debbie', 'Mucarsel-Powell Debbie'), ('Mullin Markwayne', 'Mullin Markwayne'), ('Murphy Greg', 'Murphy Greg'), ('Murphy Stephanie', 'Murphy Stephanie'), ('Nadler Jerry', 'Nadler Jerry'), ('Napolitano Grace', 'Napolitano Grace'), ('Neal Richard', 'Neal Richard'), ('Neguse Joe', 'Neguse Joe'), ('Newhouse Dan', 'Newhouse Dan'), ('Norcross Donald', 'Norcross Donald'), ('Norman Ralph', 'Norman Ralph'), ('Holmes Norton Eleanor', 'Holmes Norton Eleanor'), ('Nunes Devin', 'Nunes Devin'), ("O'Halleran Tom", "O'Halleran Tom"), ('Ocasio-Cortez Alexandria', 'Ocasio-Cortez Alexandria'), ('Olson Pete', 'Olson Pete'), ('Omar Ilhan', 'Omar Ilhan'), ('Palazzo Steven', 'Palazzo Steven'), ('Pallone Frank', 'Pallone Frank'), ('Palmer Gary', 'Palmer Gary'), ('Panetta Jimmy', 'Panetta Jimmy'), ('Pappas Chris', 'Pappas Chris'), ('Pascrell Bill', 'Pascrell Bill'), ('Payne Jr. Donald', 'Payne Jr. Donald'), ('Pelosi Nancy', 'Pelosi Nancy'), ('Pence Greg', 'Pence Greg'), ('Perlmutter Ed', 'Perlmutter Ed'), ('Perry Scott', 'Perry Scott'), ('Peters Scott', 'Peters Scott'), ('Peterson Collin', 'Peterson Collin'), ('Phillips Dean', 'Phillips Dean'), ('Pingree Chellie', 'Pingree Chellie'), ('Plaskett Stacey', 'Plaskett Stacey'), ('Pocan Mark', 'Pocan Mark'), ('Porter Katie', 'Porter Katie'), ('Posey Bill', 'Posey Bill'), ('Pressley Ayanna', 'Pressley Ayanna'), ('Price David', 'Price David'), ('Quigley Mike', 'Quigley Mike'), ('Coleman Radewagen Amata', 'Coleman Radewagen Amata'), ('Raskin Jamie', 'Raskin Jamie'), ('Ratcliffe John', 'Ratcliffe John'), ('Reed Tom', 'Reed Tom'), ('Reschenthaler Guy', 'Reschenthaler Guy'), ('Rice Kathleen', 'Rice Kathleen'), ('Rice Tom', 'Rice Tom'), ('Richmond Cedric', 'Richmond Cedric'), ('Riggleman Denver', 'Riggleman Denver'), ('Roby Martha', 'Roby Martha'), ('Roe Phil', 'Roe Phil'), ('Rogers Hal', 'Rogers Hal'), ('Rogers Mike', 'Rogers Mike'), ('Rooney Francis', 'Rooney Francis'), ('Rose John', 'Rose John'), ('Rose Max', 'Rose Max'), ('Rouda Harley', 'Rouda Harley'), ('Rouzer David', 'Rouzer David'), ('Roy Chip', 'Roy Chip'), ('Roybal-Allard Lucille', 'Roybal-Allard Lucille'), ('Ruiz Raul', 'Ruiz Raul'), ('Ruppersberger Dutch', 'Ruppersberger Dutch'), ('Rush Bobby', 'Rush Bobby'), ('Rutherford John', 'Rutherford John'), ('Ryan Tim', 'Ryan Tim'), ('Sablan Gregorio Kilili Camacho', 'Sablan Gregorio Kilili Camacho'), ('San Nicolas Michael', 'San Nicolas Michael'), ('Sanchez Linda', 'Sanchez Linda'), ('Sarbanes John', 'Sarbanes John'), ('Scalise Steve', 'Scalise Steve'), ('Gay Scanlon Mary', 'Gay Scanlon Mary'), ('Schakowsky Jan', 'Schakowsky Jan'), ('Schiff Adam', 'Schiff Adam'), ('Schneider Brad', 'Schneider Brad'), ('Schrader Kurt', 'Schrader Kurt'), ('Schrier Kim', 'Schrier Kim'), ('Schweikert David', 'Schweikert David'), ('Scott Austin', 'Scott Austin'), ('Scott David', 'Scott David'), ('Scott Bobby', 'Scott Bobby'), ('Sensenbrenner Jim', 'Sensenbrenner Jim'), ('Serrano Jose', 'Serrano Jose'), ('Sewell Terri', 'Sewell Terri'), ('Shalala Donna', 'Shalala Donna'), ('Sherman Brad', 'Sherman Brad'), ('Sherrill Mikie', 'Sherrill Mikie'), ('Shimkus John', 'Shimkus John'), ('Simpson Mike', 'Simpson Mike'), ('Sires Albio', 'Sires Albio'), ('Slotkin Elissa', 'Slotkin Elissa'), ('Torres Small Xochitl', 'Torres Small Xochitl'), ('Smith Adam', 'Smith Adam'), ('Smith Adrian', 'Smith Adrian'), ('Smith Chris', 'Smith Chris'), ('Smith Jason', 'Smith Jason'), ('Smucker Lloyd', 'Smucker Lloyd'), ('Soto Darren', 'Soto Darren'), ('Spanberger Abigail', 'Spanberger Abigail'), ('Spano Ross', 'Spano Ross'), ('Speier Jackie', 'Speier Jackie'), ('Stanton Greg', 'Stanton Greg'), ('Stauber Pete', 'Stauber Pete'), ('Stefanik Elise', 'Stefanik Elise'), ('Steil Bryan', 'Steil Bryan'), ('Steube Greg', 'Steube Greg'), ('Stevens Haley', 'Stevens Haley'), ('Stewart Chris', 'Stewart Chris'), ('Stivers Steve', 'Stivers Steve'), ('Suozzi Tom', 'Suozzi Tom'), ('Swalwell Eric', 'Swalwell Eric'), ('Takano Mark', 'Takano Mark'), ('Taylor Van', 'Taylor Van'), ('Thompson Bennie', 'Thompson Bennie'), ('Thompson Glenn', 'Thompson Glenn'), ('Thompson Mike', 'Thompson Mike'), ('Thornberry Mac', 'Thornberry Mac'), ('Tiffany Tom', 'Tiffany Tom'), ('Timmons William', 'Timmons William'), ('Tipton Scott', 'Tipton Scott'), ('Titus Dina', 'Titus Dina'), ('Tlaib Rashida', 'Tlaib Rashida'), ('Tonko Paul', 'Tonko Paul'), ('Torres Norma', 'Torres Norma'), ('Trahan Lori', 'Trahan Lori'), ('Trone David', 'Trone David'), ('Turner Mike', 'Turner Mike'), ('Underwood Lauren', 'Underwood Lauren'), ('Upton Fred', 'Upton Fred'), ('Van Drew Jeff', 'Van Drew Jeff'), ('Vargas Juan', 'Vargas Juan'), ('Veasey Marc', 'Veasey Marc'), ('Vela Filemon', 'Vela Filemon'), ('Velazquez Nydia', 'Velazquez Nydia'), ('Visclosky Pete', 'Visclosky Pete'), ('Wagner Ann', 'Wagner Ann'), ('Walberg Tim', 'Walberg Tim'), ('Walden Greg', 'Walden Greg'), ('Walker Mark', 'Walker Mark'), ('Walorski Jackie', 'Walorski Jackie'), ('Waltz Michael', 'Waltz Michael'), ('Wasserman Schultz Debbie', 'Wasserman Schultz Debbie'), ('Waters Maxine', 'Waters Maxine'), ('Watkins Steve', 'Watkins Steve'), ('Watson Coleman Bonnie', 'Watson Coleman Bonnie'), ('Weber Randy', 'Weber Randy'), ('Webster Dan', 'Webster Dan'), ('Welch Peter', 'Welch Peter'), ('Wenstrup Brad', 'Wenstrup Brad'), ('Westerman Bruce', 'Westerman Bruce'), ('Wexton Jennifer', 'Wexton Jennifer'), ('Wild Susan', 'Wild Susan'), ('Williams Roger', 'Williams Roger'), ('Wilson Joe', 'Wilson Joe'), ('Wilson Frederica', 'Wilson Frederica'), ('Wittman Rob', 'Wittman Rob'), ('Womack Steve', 'Womack Steve'), ('Woodall Rob', 'Woodall Rob'), ('Wright Ron', 'Wright Ron'), ('Yarmuth John', 'Yarmuth John'), ('Yoho Ted', 'Yoho Ted'), ('Young Don', 'Young Don'), ('Zeldin Lee', 'Zeldin Lee')], default='None', max_length=1000, verbose_name='Copatrocinador/a'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='destinatario',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('', 'N/a'), ('ACA', 'ACA'), ('BOP', 'BOP'), ('CBP', 'CBP'), ('CDC', 'CDC'), ('CRCL', 'CRCL'), ('DHS', 'DHS'), ('DOD', 'DOD'), ('DOE', 'DOE'), ('DOJ', 'DOJ'), ('DOL', 'DOL'), ('DOS', 'DOS'), ('DOT', 'DOT'), ('EMBAMEX', 'EMBAMEX'), ('EOIR', 'EOIR'), ('FEMA', 'FEMA'), ('GAO', 'GAO'), ('GEO', 'GEO'), ('HHS', 'HHS'), ('HUD', 'HUD'), ('ICE', 'ICE'), ('IG DHS', 'IG DHS'), ('Líder de la mayoría Cámara', 'Líder de la mayoría Cámara'), ('Líder de la minoría Cámara', 'Líder de la minoría Cámara'), ('Líder de la mayoría Senado', 'Líder de la mayoría Senado'), ('Líder de la minoría Senado', 'Líder de la minoría Senado'), ('Liderazgo Comité Apropiaciones Senado', 'Liderazgo Comité Apropiaciones Senado'), ('OJJDP', 'OJJDP'), ('POTUS', 'POTUS'), ('USAID', 'USAID'), ('USBA', 'USBA'), ('USCIS', 'USCIS'), ('USTR', 'USTR'), ('VPOTUS', 'VPOTUS'), ('Other', 'Other')], max_length=100),
        ),
    ]
